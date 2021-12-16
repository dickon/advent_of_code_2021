from functools import reduce
from operator import mul
def msb(v):
    # https://www.geeksforgeeks.org/find-significant-set-bit-number/
    n = v
    i = 0
    v //= 2
    while v != 0:
        v //= 2
        i += 1
    print('msb',hex(n), i)
    return i

assert msb(1) == 0
assert msb(256) == 8
assert msb(257) == 8
assert msb(0xD2FE28) == 23
assert msb(240) == 7

class Popper:
    def __init__(self, v, leading=0):
        self.v = v
        m = msb(v)+1
        rem = m % 4
        self.cursor= (m if rem == 0 else m + 4-rem)  - 1 + leading
        print(m, 'bits remainder', rem, 'cursor', self.cursor)
    def take(self, n):
        mask = ((1 << n) - 1) << (self.cursor-n+1)
        raw = self.v & mask 
        res =  raw >> (self.cursor-n+1)
        print('take', n, 'from', self.cursor, 'mask', hex(mask), 'on', hex(self.v), 'raw bits', hex(raw), '->', res)
        self.cursor -= n
        return res

t = Popper(240)
assert t.take(4) == 15
assert t.take(4) == 0

def version_sum(packet):
    x =  packet['version']
    for subp in packet.get('subpackets', []):
        x += version_sum(subp)
    return x

def parse(v, leading=0):
    d = Popper(v, leading)
    def read_packet():
        packet_version = d.take(3)
        packet_type = d.take(3)
        packet = {'type': packet_type, 'version': packet_version}
        print('headers', packet)
        match (packet_version, packet_type):
            case _, 4:
                x = 0
                while True:
                    continues = d.take(1)
                    digit = d.take(4)
                    x = (x<<4) + digit            
                    print(continues, digit, x)
                    if not continues: 
                        break
                packet['payload'] = x
            case _, _:
                # operator
                length_type = d.take(1)
                subpackets= []
                match length_type:
                    case 0:
                        total_length = d.take(15)
                        print('subpackets length', total_length)
                        cursor = d.cursor
                        while cursor - d.cursor < total_length:
                            print('cursor moved from', cursor, 'to', d.cursor, 'co we have processed', cursor - d.cursor, 'bits of', total_length)
                            subpackets.append(read_packet())
                    case 1:
                        number_of_sub_packets = d.take(11)
                        print('subpackets count', number_of_sub_packets)
                        for i in range(number_of_sub_packets):
                            subpackets.append(read_packet())
                packet['subpackets'] = subpackets
        print(packet)
        return packet        
    return read_packet()

        

r = parse(0xD2FE28)
assert r['type'] == 4
assert r['version'] == 6
assert r['payload'] == 2021

r2 = parse(0xEE00D40C823060)
assert r2 == {'type': 3, 'version': 7, 'subpackets': [{'type': 4, 'version': 2, 'payload': 1}, {'type': 4, 'version': 4, 'payload': 2}, {'type': 4, 'version': 1, 'payload': 3}]}

r3 = parse(0x38006F45291200)
assert r3 == {'type': 6, 'version': 1, 'subpackets': [{'type': 4, 'version': 6, 'payload': 10}, {'type': 4, 'version': 2, 'payload': 20}]}

r4 = parse(0x8A004A801A8002F478)
assert r4 == {'type': 2, 'version': 4, 'subpackets': [{'type': 2, 'version': 1, 'subpackets': [{'type': 2, 'version': 5, 'subpackets': [{'type': 4, 'version': 6, 'payload': 15}]}]}]}
assert version_sum(r4) ==  16

r5 = parse(0x620080001611562C8802118E34)
assert version_sum(r5) == 12


r6 = parse(0xC0015000016115A2E0802F182340)
assert version_sum(r6) == 23

r7 = parse(0xA0016C880162017C3686B18A3D4780)
assert version_sum(r7) == 31


def evaluate(packet):
    subp_values = [evaluate(x) for x in packet.get('subpackets', [])]
    match packet['type']:
        case 0: 
            return sum(subp_values)
        case 1:
            return reduce(mul, subp_values, 1)
        case 2:
            return reduce(min, subp_values, subp_values[0])
        case 3:
            return reduce(max, subp_values, subp_values[0])
        case 4:
            return packet['payload']
        case 5:
            return 1 if subp_values[0] > subp_values[1] else 0
        case 6:
            return 1 if subp_values[0] < subp_values[1] else 0
        case 7:
            return 1 if subp_values[0] == subp_values[1] else 0
        case _:
            print("ERROR: invalid packet type", packet['type'])
            return 0


assert evaluate(parse(0xC200B40A82)) == 3
assert evaluate(parse(0x04005AC33890, 4)) == 54
assert evaluate(parse(0x880086C3E88112)) == 7
assert evaluate(parse(0xCE00C43D881120)) == 9
assert evaluate(parse(0xD8005AC2A8F0)) == 1
assert evaluate(parse(0xF600BC2D8F)) == 0
assert evaluate(parse(0x9C005AC2F8F0)) == 0
assert evaluate(parse(0x9C0141080250320F1802104A08)) == 1

act = parse(0x60556F980272DCE609BC01300042622C428BC200DC128C50FCC0159E9DB9AEA86003430BE5EFA8DB0AC401A4CA4E8A3400E6CFF7518F51A554100180956198529B6A700965634F96C0B99DCF4A13DF6D200DCE801A497FF5BE5FFD6B99DE2B11250034C00F5003900B1270024009D610031400E70020C0093002980652700298051310030C00F50028802B2200809C00F999EF39C79C8800849D398CE4027CCECBDA25A00D4040198D31920C8002170DA37C660009B26EFCA204FDF10E7A85E402304E0E60066A200F4638311C440198A11B635180233023A0094C6186630C44017E500345310FF0A65B0273982C929EEC0000264180390661FC403006E2EC1D86A600F43285504CC02A9D64931293779335983D300568035200042A29C55886200FC6A8B31CE647880323E0068E6E175E9B85D72525B743005646DA57C007CE6634C354CC698689BDBF1005F7231A0FE002F91067EF2E40167B17B503E666693FD9848803106252DFAD40E63D42020041648F24460400D8ECE007CBF26F92B0949B275C9402794338B329F88DC97D608028D9982BF802327D4A9FC10B803F33BD804E7B5DDAA4356014A646D1079E8467EF702A573FAF335EB74906CF5F2ACA00B43E8A460086002A3277BA74911C9531F613009A5CCE7D8248065000402B92D47F14B97C723B953C7B22392788A7CD62C1EC00D14CC23F1D94A3D100A1C200F42A8C51A00010A847176380002110EA31C713004A366006A0200C47483109C0010F8C10AE13C9CA9BDE59080325A0068A6B4CF333949EE635B495003273F76E000BCA47E2331A9DE5D698272F722200DDE801F098EDAC7131DB58E24F5C5D300627122456E58D4C01091C7A283E00ACD34CB20426500BA7F1EBDBBD209FAC75F579ACEB3E5D8FD2DD4E300565EBEDD32AD6008CCE3A492F98E15CC013C0086A5A12E7C46761DBB8CDDBD8BE656780)
assert version_sum(act) == 871

print(evaluate(act))

