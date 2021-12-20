from pprint import pprint
from collections import Counter
import numpy as np
import math
from scipy.spatial.transform import Rotation

from constraint import Problem, RecursiveBacktrackingSolver

"""
I have no idea how to approach this!

"""


sample = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""


real = """
--- scanner 0 ---
-880,-557,778
-611,290,670
598,502,694
627,-521,631
-908,-626,915
-667,517,-416
653,-608,742
619,-567,601
-541,508,-276
-573,475,-350
616,389,617
658,483,734
-501,223,776
-92,5,101
-966,-685,-334
310,-833,-657
-879,-602,773
472,-843,-557
472,-871,-567
-510,239,817
-861,-803,-266
783,524,-377
-878,-591,-260
815,640,-317
-16,-141,-1
657,597,-394

--- scanner 1 ---
-342,623,-335
437,-326,644
-751,454,509
748,716,528
-785,566,599
53,-5,-74
513,-321,703
-749,-226,-474
588,626,-626
-20,119,90
524,-325,650
-639,-293,-580
-436,-750,548
669,671,572
-370,554,-472
-371,599,-477
528,523,-532
503,-433,-410
486,-567,-427
-541,-724,467
-433,-711,594
-689,495,689
519,-502,-310
655,503,-676
-740,-242,-433
728,797,546

--- scanner 2 ---
-447,446,-705
623,695,-536
-532,-388,322
349,542,589
-467,590,-578
-498,650,320
761,-419,-459
298,689,690
-543,645,321
534,-478,627
-93,-60,24
-570,496,-638
282,648,699
48,-137,-88
567,-404,659
-567,787,292
810,-519,-397
-618,-568,-794
576,-544,533
558,812,-569
489,712,-553
-744,-394,339
-625,-611,-753
819,-575,-440
-569,-592,-825
-626,-462,234

--- scanner 3 ---
339,-815,388
-500,420,-617
-495,-671,-609
-526,333,-506
-370,-712,502
719,347,-563
787,-838,-639
716,250,670
-338,-828,442
717,335,667
-681,683,692
-681,655,682
854,306,-541
-843,645,782
-537,-577,-492
-555,-690,-569
-496,-785,519
785,247,-677
423,-840,474
329,-909,487
-534,379,-476
771,-983,-606
-33,-41,127
631,-897,-674
554,240,687

--- scanner 4 ---
-107,-126,10
-622,461,-286
-558,-808,-479
-550,-803,612
-56,0,159
557,315,573
-377,758,630
-675,-766,-385
647,411,502
-661,-777,525
-598,-748,-498
552,667,-704
315,-485,663
-514,730,561
502,-533,608
-519,729,606
467,349,461
505,-810,-622
413,-899,-635
391,-440,662
-475,360,-235
425,559,-717
506,664,-743
-691,-769,571
394,-748,-744
-516,351,-219

--- scanner 5 ---
-738,-555,723
-662,510,693
-694,-436,671
322,-502,799
-73,73,-94
-813,-399,-583
388,-574,840
-827,-610,-513
627,856,-730
-662,414,-785
346,-644,754
724,825,401
-824,-574,-637
-653,623,561
-549,414,-712
464,-365,-561
503,-392,-428
-468,436,-812
676,746,-667
701,845,-823
715,834,446
557,790,356
520,-310,-383
-725,561,553
-741,-497,785

--- scanner 6 ---
498,-465,753
-291,-666,829
568,-977,-581
-599,740,826
708,713,795
851,686,-818
-411,-886,-379
422,-891,-574
92,-196,0
441,-978,-422
-750,631,807
813,739,714
816,700,668
560,-506,573
-568,438,-378
-481,-844,-293
-553,-910,-334
-389,430,-288
-5,-12,128
464,-577,663
702,614,-783
-564,308,-288
-336,-667,905
-661,618,715
-384,-612,718
675,645,-768

--- scanner 7 ---
650,-645,583
-548,631,-805
631,-833,-572
645,-597,667
607,449,671
-856,723,531
-159,-19,-111
673,363,591
-380,-625,689
663,473,-639
-506,792,-879
-445,-665,687
-932,-509,-946
695,-721,-572
-21,-134,12
-897,783,484
553,324,644
485,498,-648
-743,740,579
-762,-575,-965
736,-825,-707
-394,-443,661
-834,-564,-882
-458,582,-873
813,-587,573
580,330,-627

--- scanner 8 ---
-535,-646,373
49,64,7
712,545,482
-413,428,-787
-564,-583,-650
-502,520,-774
845,-611,346
778,-513,-798
-872,406,510
490,330,-589
-564,409,-896
-33,-62,-155
320,432,-615
-543,-676,419
-546,-660,-537
776,-475,287
620,491,492
762,-546,-943
-827,330,511
-504,-543,-631
710,-589,387
-509,-535,460
469,421,-592
622,-478,-857
443,548,498
-779,517,456

--- scanner 9 ---
-691,697,-504
606,-525,-831
-708,312,884
604,-422,-859
-879,-787,632
-805,-755,599
582,-530,-757
-864,331,826
-672,625,-560
369,295,745
394,311,803
865,-899,630
-889,-467,-679
-895,-450,-467
-715,666,-553
-764,269,875
814,-826,548
-739,-661,641
669,693,-398
835,-907,511
323,329,771
503,633,-342
41,-84,54
459,696,-317
-821,-362,-561

--- scanner 10 ---
700,-673,733
565,566,545
-655,-386,666
-35,27,-40
-440,-441,-330
-588,352,-383
432,723,-488
-529,-330,581
-528,-379,-456
739,-726,613
280,-566,-837
-500,-339,-395
733,545,640
340,-613,-796
271,797,-446
614,-753,667
-435,429,515
-383,391,594
-520,-401,719
590,557,723
-488,390,504
-545,334,-423
481,791,-398
-646,448,-404
323,-661,-683

--- scanner 11 ---
-523,667,-763
-761,-605,298
553,-663,332
748,-670,-550
427,451,-834
481,495,-926
-234,733,382
-234,552,415
746,522,514
876,432,518
140,27,-65
-561,474,-740
-537,-491,-834
-571,597,-800
754,432,693
-690,-669,445
-325,661,340
491,494,-716
751,-761,-571
-547,-647,-812
444,-682,483
-740,-625,380
-476,-528,-761
725,-659,-401
566,-571,421

--- scanner 12 ---
534,-664,530
506,566,785
-651,-482,723
-531,374,-562
933,613,-583
444,-668,400
-658,400,528
-749,-896,-575
535,-821,-794
-7,-29,73
-647,251,551
-534,643,-546
-559,-571,710
-749,421,525
463,684,849
843,657,-425
106,-110,-59
507,776,795
-670,-633,832
449,-751,-752
-673,-941,-574
490,-679,-818
-588,551,-556
888,648,-416
444,-843,522
-562,-848,-520

--- scanner 13 ---
661,639,-831
-683,-841,-609
-555,-518,629
859,376,374
-559,681,-427
713,528,-837
-711,637,549
-750,-824,-776
-401,588,-408
-477,611,-393
-606,645,684
787,387,291
720,-842,-411
529,-822,-422
-655,-918,-710
-638,-661,617
-670,533,684
483,-770,383
6,-65,-36
531,-980,377
502,-841,-406
755,671,-764
-460,-686,608
129,9,74
957,321,310
573,-819,451

--- scanner 14 ---
538,411,-771
-675,874,471
-837,-690,-720
348,-523,-489
316,-298,707
-523,-771,931
-731,696,526
-692,829,553
431,508,964
-543,-739,767
499,501,861
559,425,-605
414,-293,789
386,549,964
363,-287,605
-413,-702,878
-636,-698,-697
414,-514,-578
-494,434,-684
-568,527,-695
-124,-5,130
-690,-633,-734
330,-424,-459
-519,590,-585
616,362,-777

--- scanner 15 ---
-391,431,-743
592,-436,-482
-474,-609,-535
516,-464,478
706,705,-770
512,-502,-568
-7,-73,54
-789,642,691
-452,-577,411
-346,407,-601
-34,95,-83
600,-459,526
732,669,629
678,679,721
-699,800,735
-744,809,726
893,650,-818
-305,473,-673
675,663,452
-592,-640,462
817,651,-863
-422,-653,-654
610,-296,468
539,-556,-443
-360,-656,-596
-584,-568,524

--- scanner 16 ---
711,389,-690
-640,572,459
-579,475,-510
-447,-653,-613
-587,452,498
-663,480,-462
690,-772,542
633,-758,-703
-667,518,584
652,640,633
576,430,-586
720,-726,550
655,-799,-838
643,462,608
-569,312,-452
-501,-663,-705
576,494,-698
579,-685,516
631,545,465
519,-858,-769
90,60,61
-362,-635,879
-504,-647,-436
-286,-634,834
-473,-689,786

--- scanner 17 ---
-670,636,302
433,641,-915
-454,541,-877
-590,-680,-722
-678,601,506
-31,3,-135
741,657,647
467,-357,313
685,-356,318
496,-218,-470
-673,-537,-710
-465,488,-838
877,642,566
448,-428,-476
-495,-512,-701
88,176,-48
538,-379,-544
-690,-280,617
-585,672,383
473,598,-933
-718,-357,516
775,649,632
-785,-374,683
494,-376,329
-544,436,-876
454,699,-819

--- scanner 18 ---
484,-782,-326
-828,475,486
725,568,651
-879,557,413
-467,-815,-419
-89,-133,-37
-596,-830,782
-760,408,-799
791,526,557
747,648,-673
584,-792,-488
-849,438,405
824,691,-831
-618,-932,890
764,575,-799
-459,-820,-543
807,-634,950
-620,-904,787
574,-820,-488
-619,479,-825
-80,55,77
881,-540,862
-435,-841,-339
875,-752,845
865,559,525
-752,370,-817

--- scanner 19 ---
278,-537,-508
-527,901,494
-98,173,111
-619,812,507
-666,-665,425
-521,788,-749
-585,935,-820
-86,41,-48
245,-556,-553
-508,750,385
322,542,-664
561,768,744
383,527,-541
-565,853,-799
508,-459,843
-539,-557,412
361,-358,894
-620,-662,386
-710,-796,-605
484,750,631
323,514,-585
444,810,650
402,-349,910
-723,-641,-724
420,-563,-614
-608,-760,-696

--- scanner 20 ---
431,-704,-682
-147,26,66
-696,-545,-708
426,-620,-634
445,535,-446
381,535,-558
-702,-488,-531
560,610,790
-848,614,-306
505,548,698
-907,478,-375
536,492,879
-483,757,852
-533,901,844
-807,592,-441
-477,-539,567
414,-641,417
-625,873,822
-593,-578,691
464,-627,539
-28,-46,-73
340,670,-454
263,-610,-692
520,-680,479
-466,-669,669
-712,-542,-439

--- scanner 21 ---
-266,486,648
578,-611,-708
-818,735,-464
-759,-456,-789
-691,-545,727
407,-548,624
-407,414,606
496,-666,600
-706,-562,774
-278,471,630
634,761,-544
747,571,696
-676,657,-492
-698,-556,767
63,-153,67
807,624,640
525,774,-558
626,-676,-624
624,-631,-871
-627,-432,-708
550,778,-542
-734,-461,-727
-742,786,-431
869,585,746
588,-604,655

--- scanner 22 ---
-658,443,-873
688,-773,-852
94,86,-43
365,435,679
316,-602,678
-101,19,38
-343,-416,-420
-561,407,-825
-462,383,561
-405,-615,824
-359,-493,-424
-404,-525,719
-443,-536,772
636,-689,-733
749,-675,-833
372,-687,552
325,374,707
387,-740,687
-564,-448,-433
623,594,-764
-348,402,662
531,670,-784
629,524,-772
427,309,767
65,-103,67
-684,443,-722
-366,362,619

--- scanner 23 ---
435,-295,689
376,-489,-751
-776,528,-600
756,497,-606
-659,601,725
-827,580,630
342,-579,-639
426,-366,551
-413,-413,-550
-506,-524,-604
394,425,766
-833,-691,657
-684,592,547
341,464,755
-794,-638,537
785,355,-582
-750,639,-687
561,-351,604
-144,111,172
-458,-337,-549
289,426,676
25,-25,67
438,-669,-710
-742,669,-641
-708,-718,603
757,492,-651

--- scanner 24 ---
-111,-95,111
361,-657,765
-582,632,729
505,-558,752
-589,-581,768
-530,716,848
-893,-431,-711
748,709,611
-831,683,-691
657,337,-287
-853,-492,-683
-791,-366,-771
740,-662,-280
63,-50,-45
-846,630,-556
382,-527,879
737,-458,-369
819,-451,-281
656,803,580
701,756,570
567,372,-315
645,506,-298
-595,-651,760
-469,618,829
-902,545,-682
-687,-727,780

--- scanner 25 ---
538,-604,597
-69,170,-40
486,-485,641
424,-543,644
-475,-696,544
455,-396,-443
-800,563,438
-448,-571,490
498,456,-351
688,967,784
369,-466,-485
-528,-657,424
-587,479,-752
-497,575,-823
410,-538,-419
598,939,749
676,956,615
650,437,-438
657,583,-352
63,30,10
-677,513,-864
-753,-276,-663
-642,-369,-717
-815,698,491
-871,572,576
-829,-321,-662

--- scanner 26 ---
603,-662,-789
921,616,705
838,688,716
-837,496,-760
528,-777,447
541,-717,-697
-711,-791,683
663,-882,455
-705,248,837
-627,-796,635
-733,234,655
-634,-758,-538
902,786,771
485,-686,-878
117,-22,-80
528,-841,559
613,562,-659
-731,299,615
-824,482,-651
-648,-808,-416
548,646,-707
-687,-702,-478
-617,-959,693
-841,480,-735
43,-158,54
568,809,-661

--- scanner 27 ---
-688,503,355
602,-599,627
633,-605,-905
638,-650,-906
666,756,-490
-8,72,-119
-707,-336,446
-789,531,278
-474,551,-638
491,-686,601
461,-640,593
-400,-616,-904
-406,-404,-887
-555,636,-674
-678,543,-603
550,631,678
775,-581,-934
-697,-364,446
-855,436,372
704,677,-438
705,767,-543
-191,149,-166
-474,-522,-992
538,548,535
-797,-374,284
529,726,510

--- scanner 28 ---
-713,-683,864
710,829,-871
569,-596,779
888,752,850
561,-775,869
-637,-474,-537
-425,637,-643
-779,-611,823
-544,681,380
-474,747,-706
126,-94,-57
88,32,118
525,-912,-725
480,-912,-684
824,634,807
-598,-501,-404
653,657,-808
-755,-753,778
-400,736,-799
-581,-419,-359
632,823,-822
439,-600,869
593,-809,-732
834,844,806
-386,725,470
-377,716,425

--- scanner 29 ---
423,-939,368
496,689,481
907,-613,-518
-502,-588,597
492,-886,258
-442,-468,-499
-476,281,-751
680,570,-569
561,726,535
-322,-453,-521
671,481,-503
-15,4,-8
-48,-164,-115
901,-797,-569
-445,-665,573
504,712,682
-417,456,-807
-398,384,755
-320,-554,-541
896,-715,-471
-557,396,-782
-571,416,772
-454,-643,535
455,-775,388
770,451,-485
-477,321,741
"""

def parse(text):
    scanner = None
    scanners = {}
    for line in text.split('\n'):
        if not line.strip(): continue
        spl = line.split()
        if len(spl) == 4 and spl[0] == '---' and spl[-1] == '---':
            scanner = int(spl[2])
            scanners[scanner] = []
        else:
            cspl = line.split(',')
            if len(cspl) == 3:
                scanners[scanner].append( np.hstack( ( [int(x) for x in cspl], 1 )))
    return list(scanners.values())

def make_rotation(rx, ry, rz):
    rxr = Rotation.from_rotvec(rx*np.pi/2 * np.array([1,0,0]))
    ryr = Rotation.from_rotvec(ry*np.pi/2 * np.array([0,1,0]))
    rzr = Rotation.from_rotvec(rz*np.pi/2 * np.array([0,0,1]))
    r = rxr*ryr*rzr
    faxis = [ r.apply(v) for v in [[1,0,0], [0,1,0], [0,0,1]] ]
    axis = tuple([ tuple([round(v) for v in x]) for x in faxis])
    m =  np.array([
        [ axis[0][0], axis[0][1], axis[0][2], 0],
        [ axis[1][0], axis[1][1], axis[1][2], 0],
        [ axis[2][0], axis[2][1], axis[2][2], 0],
        [ 0, 0, 0, 1]
    ])
    assert m.shape == (4,4)
    assert m.ndim == 2
    #print(f'rotate {rx} {ry} {rz} =\n{m}')
    return m

assert (make_rotation(0,0,0) == np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1')).all()
assert (make_rotation(4,4,4) == np.matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1')).all()
assert (make_rotation(1,0,0) == np.matrix('1 0 0 0; 0 0 1 0; 0 -1 0 0; 0 0 0 1')).all()


orientations_map = {}
for rx in range(4):
    for ry in range(4):
        for rz in range(4):            
            m  = make_rotation(rx,ry,rz)            
            orientations_map.setdefault(repr(m), (m, list()))[1].append( (rx,ry,rz))

#pprint(list(orientations_map.values()))
assert len(orientations_map) == 24
orientations = list(orientations_map.values())

def homogenous(x):
    return np.array(list(x)+[1])

def homogenous_y(x):
    return np.array([ 
        [x[0]],
        [x[1]],
        [x[2]],
        [1]
    ])

def homorepr(x):
    print(x)
    assert x[0,3] == 1
    return f'({x[0]}, {x[1]}, {x[2]})'

def align(scanners, verbose=False):
    transformations = {}
    def dump(i, j):
        orientation, deltas = transformations[(i,j)]
        _, (rx,ry, rz, matrix, r) = orientations[orientation]
        # print(rx,ry,rz)
        # print(matrix)
        # we now know how to convert between scanner i and scanner j coordinate
        intersections = 0
        s2_coords_in_s1_space = []

        for pos in scanners[j]:
            coords = (
                round(pos[0]*matrix[0][0] + pos[1]*matrix[1][0] + pos[2]*matrix[2][0]+ deltas[0]),
                round(pos[0]*matrix[0][1] + pos[1]*matrix[1][1] + pos[2]*matrix[2][1] + deltas[1]),
                round(pos[0]*matrix[0][2] + pos[1]*matrix[1][2] + pos[2]*matrix[2][2] + deltas[2])
            )
            if coords in scanners[i]:
                intersections += 1
            s2_coords_in_s1_space.append( coords )
            print(pos, coords, '*' if coords in scanners[i] else '')
        print('intersections', i,j, intersections)                
        return s2_coords_in_s1_space
    if False:
        array = np.array
        transformations = {(0, 1): array([[   -1,     0,     0,    68],
       [    0,     1,     0, -1246],
       [    0,     0,    -1,   -43],
       [    0,     0,     0,     1]]),
 (1, 0): array([[  -1,    0,    0,   68],
       [   0,    1,    0, 1246],
       [   0,    0,   -1,  -43],
       [   0,    0,    0,    1]]),
 (1, 3): array([[    1,     0,     0,   160],
       [    0,     1,     0, -1134],
       [    0,     0,     1,   -23],
       [    0,     0,     0,     1]]),
 (1, 4): array([[    0,     1,     0,    88],
       [    0,     0,    -1,   113],
       [   -1,     0,     0, -1104],
       [    0,     0,     0,     1]]),
 (2, 4): array([[   0,    1,    0, 1125],
       [   1,    0,    0, -168],
       [   0,    0,   -1,   72],
       [   0,    0,    0,    1]]),
 (3, 1): array([[   1,    0,    0, -160],
       [   0,    1,    0, 1134],
       [   0,    0,    1,   23],
       [   0,    0,    0,    1]]),
 (4, 1): array([[    0,     0,    -1, -1104],
       [    1,     0,     0,   -88],
       [    0,    -1,     0,   113],
       [    0,     0,     0,     1]]),
 (4, 2): array([[    0,     1,     0,   168],
       [    1,     0,     0, -1125],
       [    0,     0,    -1,    72],
       [    0,     0,     0,     1]])}
    else:
        print()
        print('there are', len(scanners), 'distinct scanners')
        changes = False
        failed = set()
        for i, s1 in list(enumerate(scanners)):
            for j, s2 in list(enumerate(scanners)):
                if j != i and (i,j) not in failed:
                    #if (i,j) != (1,4): continue
                    found = False
                    if (i,j) in transformations:
                        continue
                    print('compare', i, j)
                    pprint(transformations)
                    for o in range(len(orientations)):
                        #if o != 8: continue
                        if found: break
                        if verbose or 1:
                            print(f'{i}->{j} trying orientation', o)
                        m, _ = orientations[o]
                        if verbose:
                            print(f'orientation {o} is:\n{m}\n')
                        for s1i in range(len(s1)):
                            alpha = s1[s1i]
                            assert alpha.shape == (4,)
                            assert alpha[3] == 1
                            for s2i, pos in enumerate(s2):    
                                if verbose:
                                    print(f"let us try to align {s1i}:{alpha}(in s1 space) with {s2i}:{pos} on orientation {o}")                                
                                beta = np.matmul(m,  pos.transpose())
                                if verbose:
                                    print(f's2 pos rotated s1 space (beta)={beta}')
                                assert beta.shape == (4,)
                                # we want to find the transformation M such that:
                                #     alpha = M*pos
                                #  where M is the rotation matrix with a translation delta added at [0,3], [1,3], [2,3]
                                #  Expanding the cross product that gives us:
                                # alpha[0] =  m[0, 0]*beta[0] + m[0,1]*beta[1] + m[0,2]*beta[2] + T[0]*1
                                #   rearranging:
                                #    T[0] = alpha[0] -m[0, 0]*beta[0] + m[0,1]*beta[1] + m[0,2]*beta[2]
                                delta0 = alpha[0] - (m[0,0]*pos[0] + m[0,1]*pos[1] + m[0,2]*pos[2])
                                delta1 = alpha[1] - (m[1,0]*pos[0] + m[1,1]*pos[1] + m[1,2]*pos[2])
                                delta2 = alpha[2] - (m[2,0]*pos[0] + m[2,1]*pos[1] + m[2,2]*pos[2])
                                
                                if verbose:
                                    print(f"candidate delta vector={delta0}, {delta1}, {delta2}")
                                mtrans = m.copy()
                                mtrans[0, 3] = delta0
                                mtrans[1, 3] = delta1
                                mtrans[2, 3] = delta2
                                mtrans = mtrans.astype(int)
                                if verbose:
                                    print(f'translation matrix:\n{mtrans}')
                                alpha2 = np.matmul(mtrans, homogenous_y(pos)).transpose()
                                if verbose:
                                    print(f'alpha={alpha} beta moved to alpha by translation matrix={alpha2}')
                                assert (alpha == alpha2).all()

                                # the [0] next line is to convert the 1x4 matrix to a 4 vector
                                s2_in_candidate_s1_space = [np.matmul(mtrans, homogenous_y(x)).transpose()[0] for x in s2]
                                #assert s2_in_candidate_s1_space[0].shape == (4,)
                                if verbose and True:
                                    print(f's2 in candidate s1 space={s2_in_candidate_s1_space}')
                                matches = 0
                                for gi, g in enumerate(s1):
                                    for hi, h in enumerate(s2_in_candidate_s1_space):
                                        if (g==h).all():
                                            if verbose:
                                                print('match', gi, g, 'to',hi, h)
                                            matches += 1
                                            break
                                if verbose:
                                    print(f"matches {matches}")

                                if matches >= 12:
                                    print(f'match up in orientation {o} stating from s1 index {s1i} delta is {delta0},{delta1},{delta2} hits {matches}')
                                    print(mtrans)
                                    transformations[(i,j)]= mtrans
                                    transformations[(j,i)]= np.linalg.inv(mtrans).astype(int)
                                    found = True
                                    break
                            if found: 
                                break
                        if found:
                            break
                    if not found:
                        failed.add( (i,j))
                        failed.add( (j,i))
    while True:
        pprint(transformations)
        work = False
        for i in range(1,len(scanners)):
            if (0,i) not in transformations:
                for j in range(len(scanners)):
                    if (0, j) in transformations and (j, i) in transformations:
                        print(f'we want to calc 0->{i} using 0->{j} and {j}->{i}')
                        # We want to work out 0 -> i, and we know 0 -> j and j -> i
                        m0j = transformations[ (0,j) ]
                        mji = transformations[ (j,i) ]
                        m = np.matmul(m0j, mji)
                        print(m)
                        transformations[(0,i)] = m
                        work = True
        if not work:
            break
    pprint(transformations)
    # assert transformations[(0,1)][1] == (68, -1246, -43)
    # assert repr(transformations[(0,4)][1]) == 'array([  -20., -1133.,  1061.])'
    # assert repr(transformations[(0,3)][1]) == 'array([  -92., -2380.,   -20.])'
    # #assert repr(transformations[(0,2)][1]) == 'array([ 1105., -1205., 1229.])'
    locs = {}
    for pos in scanners[0]:
        locs[tuple(pos)]= list([0])
    for i in range(1, len(scanners)):
        for pos in scanners[i]:
            post = np.matmul(transformations[(0,i)], pos.transpose()).transpose()

            locs.setdefault(tuple(post), list())
            locs[tuple(post)].append(i)
    pprint(locs)
    print(len(locs))



#align(parse(sample))
align(parse(real))
