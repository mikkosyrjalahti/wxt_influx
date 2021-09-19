import unittest
import wxt_to_influx

class TestConv(unittest.TestCase):
    def test_ok_line(self):
        line="0R0,Dn=050D,Dm=053D,Dx=058D,Sn=0.8M,Sm=1.0M,Sx=1.2M,Ta=8.5C,Tp=10.6C,Ua=62.1P,Pa=1016.7H,Rc=0.00M,Rd=0s,Ri=0.0M,Hc=0.0M,Hd=0s,Hi=0.0M,Rp=0.0M,Hp=0.0M,Th=10.0C,Vh=0.0N,Vs=20.2V,Vr=3.499V"

        res = wxt_to_influx.wxt_line_to_influx_line(line)
        self.assertEqual(res,
                         'wxt_artjarvi D=50.0 D=53.0 D=58.0 S=0.8 S=1.0 S=1.2 T=8.5 T=10.6 U=62.1 P=1016.7 R=0.0 R=0.0 R=0.0 H=0.0 H=0.0 H=0.0 R=0.0 H=0.0 T=10.0 V=0.0 V=20.2 V=3.499')

    def test_empty_line(self):
        line = ""
        res = wxt_to_influx.wxt_line_to_influx_line(line)
        print(res)
        self.assertEqual(res, None)

if __name__ == '__main__':
    unittest.main()

