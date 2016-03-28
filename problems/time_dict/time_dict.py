# timedict.py

import datetime
import bisect
import unittest
import collections


class TimeDict():

    d = collections.defaultdict(lambda: ([], []))

    def get(self, key, t):
        i = bisect.bisect_right(self.d[key][0], t)
        if i:
            return self.d[key][1][i-1]
        else:
            raise KeyError()

    def set(self, key, value):
        self.d[key][0].append(datetime.datetime.now())
        self.d[key][1].append(value)


class TimeDictTest(unittest.TestCase):

    def test(self):
        d = TimeDict()
        t0 = datetime.datetime.now()
        d.set("a", 1)
        t1 = datetime.datetime.now()
        d.set("a", 2)
        t2 = datetime.datetime.now()
        d.set("b", 3)
        t3 = datetime.datetime.now()
        with self.assertRaises(KeyError):
                d.get("a", t0)
        self.assertEqual(d.get("a", datetime.datetime.now()), 2)
        self.assertEqual(d.get("a", t1), 1)
        self.assertEqual(d.get("b", t3), 3)

if __name__ == "__main__":
    unittest.main()
