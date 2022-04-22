class hrRunZones:
    def __init__(self, avgRunHR, hrBounds):
        import pandas as pd
        self.ftRunHR = 0.95 * avgRunHR
        self.z1 = [hrBounds[0], round(0.85 * self.ftRunHR, 0)]
        self.z2 = [round(0.85 * self.ftRunHR, 0), round(0.90 * self.ftRunHR, 0)]
        self.z3 = [round(0.90 * self.ftRunHR, 0), round(0.95 * self.ftRunHR, 0)]
        self.z4 = [round(0.95 * self.ftRunHR, 0), round(1.0 * self.ftRunHR, 0)]
        self.z5a = [round(1.0 * self.ftRunHR, 0), round(1.03 * self.ftRunHR, 0)]
        self.z5b = [round(1.03 * self.ftRunHR, 0), round(1.06 * self.ftRunHR, 0)]
        self.z5c = [round(1.06 * self.ftRunHR, 0), hrBounds[1]]
        self.list = [self.z1, self.z2, self.z3, self.z4, self.z5a, self.z5b, self.z5c]
        self.df = pd.DataFrame(
            self.list,
            columns = ['lower bound', 'upper bound'],
            index = ['1', '2', '3', '4', '5a', '5b', '5c']
        )

    def summary(self):
        print('Run HR Zone 1 is:', self.z1, 'BPM')
        print('Run HR Zone 2 is:', self.z2, 'BPM')
        print('Run HR Zone 3 is:', self.z3, 'BPM')
        print('Run HR Zone 4 is:', self.z4, 'BPM')
        print('Run HR Zone 5a is:', self.z5a, 'BPM')
        print('Run HR Zone 5b is:', self.z5b, 'BPM')
        print('Run HR Zone 5c is:', self.z5c, 'BPM')

class runPaceZones:
    def __init__(self, avgRunPace):
        import pandas as pd
        import datetime as datetime
        avgRunPace = datetime.timedelta(minutes=datetime.datetime.strptime(avgRunPace, '%M:%S').minute,
                                        seconds=datetime.datetime.strptime(avgRunPace, '%M:%S').second).total_seconds()

        self.ftRunPace = 1.05 * avgRunPace
        self.z1 = [round(1.29 * self.ftRunPace, 0), 600]
        self.z2 = [round(1.13 * self.ftRunPace, 0), round(1.29 * self.ftRunPace, 0)]
        self.z3 = [round(1.05 * self.ftRunPace, 0), round(1.13 * self.ftRunPace, 0)]
        self.z4 = [round(1.0 * self.ftRunPace, 0), round(1.05 * self.ftRunPace, 0)]
        self.z5a = [round(0.96 * self.ftRunPace, 0), round(1.0 * self.ftRunPace, 0)]
        self.z5b = [round(0.9 * self.ftRunPace, 0), round(0.96 * self.ftRunPace, 0)]
        self.z5c = [180, round(0.9 * self.ftRunPace, 0)]
        self.list = [self.z1, self.z2, self.z3, self.z4, self.z5a, self.z5b, self.z5c]
        self.df = pd.DataFrame(
            self.list,
            columns=['lower bound', 'upper bound'],
            index=['1', '2', '3', '4', '5a', '5b', '5c']
        )

    def summary(self):
        import datetime as datetime
        print('Run Pace Zone 1 is: [', self.z1[0], '-', datetime.timedelta(seconds=self.z1[1]), '] min/km to')
        print('Run Pace Zone 2 is: [', datetime.timedelta(seconds=self.z2[0]), '-', datetime.timedelta(seconds=self.z2[1]), '] min/km')
        print('Run Pace Zone 3 is: [', datetime.timedelta(seconds=self.z3[0]), '-', datetime.timedelta(seconds=self.z3[1]), '] min/km')
        print('Run Pace Zone 4 is: [', datetime.timedelta(seconds=self.z4[0]), '-', datetime.timedelta(seconds=self.z4[1]), '] min/km')
        print('Run Pace Zone 5a is: [', datetime.timedelta(seconds=self.z5a[0]), '-', datetime.timedelta(seconds=self.z5a[1]), '] min/km')
        print('Run Pace Zone 5b is: [', datetime.timedelta(seconds=self.z5b[0]), '-', datetime.timedelta(seconds=self.z5b[1]), '] min/km')
        print('Run Pace Zone 5c is: [',datetime.timedelta(seconds=self.z5c[0]), '-', self.z5c[1],  '] min/km')

class hrBikeZones:
    def __init__(self, avgBikeHR, hrBounds):
        import pandas as pd
        self.ftBikeHR = 0.95 * avgBikeHR
        self.z1 = [hrBounds[0], round(0.81 * self.ftBikeHR, 0)]
        self.z2 = [round(0.81 * self.ftBikeHR, 0), round(0.90 * self.ftBikeHR, 0)]
        self.z3 = [round(0.90 * self.ftBikeHR, 0), round(0.94 * self.ftBikeHR, 0)]
        self.z4 = [round(0.94 * self.ftBikeHR, 0), round(1.0 * self.ftBikeHR, 0)]
        self.z5a = [round(1.0 * self.ftBikeHR, 0), round(1.03 * self.ftBikeHR, 0)]
        self.z5b = [round(1.03 * self.ftBikeHR, 0), round(1.06 * self.ftBikeHR, 0)]
        self.z5c = [round(1.06 * self.ftBikeHR, 0), hrBounds[1]]
        self.list = [self.z1, self.z2, self.z3, self.z4, self.z5a, self.z5b, self.z5c]
        self.df = pd.DataFrame(
            self.list,
            columns=['lower bound', 'upper bound'],
            index=['1', '2', '3', '4', '5a', '5b', '5c']
        )

class powerBikeZones:
    def __init__(self, avgBikePower):
        import pandas as pd
        self.ftBikePower = 0.95 * avgBikePower
        self.z1 = [80, round(0.55 * self.ftBikePower, 0)]
        self.z2 = [round(0.55 * self.ftBikePower, 0), round(0.75 * self.ftBikePower, 0)]
        self.z3 = [round(0.75 * self.ftBikePower, 0), round(0.9 * self.ftBikePower, 0)]
        self.z4 = [round(0.9 * self.ftBikePower, 0), round(1.05 * self.ftBikePower, 0)]
        self.z5 = [round(1.05 * self.ftBikePower, 0), round(1.2 * self.ftBikePower, 0)]
        self.z6 = [round(1.2 * self.ftBikePower, 0), 1200]
        self.list = [self.z1, self.z2, self.z3, self.z4, self.z5, self.z6]
        self.df = pd.DataFrame(
            self.list,
            columns=['lower bound', 'upper bound'],
            index=['1', '2', '3', '4', '5', '6']
        )

class swimPaceZones:
    def __init__(self, swimTestResult):
        import pandas as pd
        import datetime as datetime

        testResult = datetime.timedelta(minutes=datetime.datetime.strptime(swimTestResult, '%M:%S').minute,
                                            seconds=datetime.datetime.strptime(swimTestResult,
                                                                               '%M:%S').second).total_seconds()
        self.ftSwimPace = 1.05 * testResult / 10

        class RangeDict(dict):
            def __getitem__(self, item):
                if not isinstance(item, range):
                    for key in self:
                        if item in key:
                            return self[key]
                    raise KeyError('Test result not in correct range.')
                else:
                    return super().__getitem__(item)

        self.paceLookup = RangeDict(
            {range(914, 943): [[180, 116], [116, 109], [109, 102], [102, 96], [96, 92], [92, 85], [85, 30]],
             range(943, 969): [[180, 118], [118, 112], [112, 104], [104, 98], [98, 94], [94, 87], [87, 30]],
             range(969,999): [[180, 122], [122, 115], [115, 107], [107, 101], [101, 97], [97, 90], [90, 30]],
             range(999,1027): [[180, 124], [124, 117], [117, 109], [109, 103], [103, 99], [99, 92], [92, 30]],
             range(1027,1059): [[180, 129], [129, 122], [122, 113], [113, 107], [107, 103], [103, 95], [95, 30]],
             range(1059,1093): [[180, 133], [133, 125], [125, 117], [117, 110], [110, 106], [106, 98], [98, 30]],
             range(1093,1129): [[180, 138], [138, 130], [130, 121], [121, 114], [114, 110], [110, 102], [102, 30]],
             range(1129,1167): [[180, 141], [141, 133], [133, 124], [124, 117], [117, 113], [113, 104], [104, 30]],
             range(1167,1207): [[180, 146], [146, 138], [138, 128], [128, 121], [121, 116], [116, 108], [108, 30]],
             range(1207,1251): [[180, 151], [151, 142], [142, 132], [132, 125], [125, 120], [120, 112], [112, 30]],
             range(1251,1298): [[180, 157], [157, 148], [148, 138], [138, 130], [130, 125], [125, 116], [116, 30]],
             range(1298,1348): [[180, 162], [162, 153], [153, 142], [142, 134], [134, 129], [129, 120], [120, 30]],
             range(1348,1403): [[180, 168], [168, 158], [158, 147], [147, 139], [139, 134], [134, 124], [124, 30]]}
            )

        self.list = [self.paceLookup[testResult][0],
                     self.paceLookup[testResult][1],
                     self.paceLookup[testResult][2],
                     self.paceLookup[testResult][3],
                     self.paceLookup[testResult][4],
                     self.paceLookup[testResult][5],
                     self.paceLookup[testResult][6]
                     ]
        self.df = pd.DataFrame(
            self.list,
            columns=['lower bound', 'upper bound'],
            index=['1', '2', '3', '4', '5a', '5b', '5c']
        )