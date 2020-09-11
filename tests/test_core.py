import unittest
import scipy
import numpy as np
from SecondOrderElec import LP, BP, HP, Notch

# we can't really test Second_Order_LTI so we will check the inheriting class
class test_LP(unittest.TestCase):
    def get_one(self, T0=0.8, m=0.2, w0=6000):
        return LP(T0, m, w0)

    def test_num(self):
        filter_instance = self.get_one()
        num = filter_instance.num
        self.assertIsInstance(num, (float, int))

    def test_den(self):
        filter_instance = self.get_one()
        den = filter_instance.den
        print(den)
        self.assertEqual(len(den), 3)

    def test_lti(self):
        filter_instance = self.get_one()
        lti = filter_instance.lti
        self.assertIsInstance(lti, scipy.signal.lti)

    def test_wr(self):
        filter_instance = self.get_one()
        wr = filter_instance.wr
        self.assertIsInstance(wr, (float, int))

    def test_MdB(self):
        filter_instance = self.get_one()
        MdB = filter_instance.MdB
        self.assertIsInstance(MdB, (float, int))

    def test_fresqresp(self):
        filter_instance = self.get_one()
        w = np.logspace(1, 4, 1000)
        t, s = filter_instance.freqresp(w=w, plot=False)
        self.assertIsInstance(t, np.ndarray)
        self.assertIsInstance(s, np.ndarray)
        self.assertEqual(len(t), len(s))

    def test_output(self):
        filter_instance = self.get_one(w0=6)

        x = np.linspace(1, 100, 10000)
        y = np.sin(x * 1000000000)  # noisy sinusoidal

        t, s, state_vector = filter_instance.output(U=y, T=x, plot=False)
        debugvalue = np.zeros((10000,))
        self.assertIsInstance(t, np.ndarray)
        self.assertIsInstance(s, np.ndarray)
        self.assertIsInstance(state_vector, np.ndarray)
        for e1, e2 in zip(s, debugvalue):
            with self.subTest(e1=e1, e2=e2):
                self.assertAlmostEqual(e1, e2, places=2)

    def test_step(self):
        filter_instance = self.get_one()
        t, s = filter_instance.step(plot=False)
        self.assertIsInstance(t, np.ndarray)
        self.assertIsInstance(s, np.ndarray)

    def test_pzmap(self):
        filter_instance = self.get_one()
        poles, zeros = filter_instance.pzmap(plot=False)
        self.assertIsInstance(poles, np.ndarray)
        self.assertIsInstance(zeros, np.ndarray)
        self.assertEqual(len(poles), 2)
        self.assertEqual(len(zeros), 0)

    def test_R(self):
        filter_instance = self.get_one()
        R = filter_instance.R
        self.assertIsInstance(R, (float, int))

    def test_wp(self):
        filter_instance = self.get_one()
        wp = filter_instance.wp
        self.assertIsInstance(wp, (float, int))

    def test_Tp(self):
        filter_instance = self.get_one()
        Tp = filter_instance.Tp
        self.assertIsInstance(Tp, (float, int))

    def test_Q(self):
        filter_instance = self.get_one()
        Q = filter_instance.Q
        self.assertIsInstance(Q, (float, int))


class test_BP(unittest.TestCase):
    def get_one(self, Tm=1.1, m=0.2, w0=6000):
        return BP(Tm, m, w0)

    def test_num(self):
        filter_instance = self.get_one()
        num = filter_instance.num
        self.assertIsInstance(num, np.ndarray)

    def test_den(self):
        filter_instance = self.get_one()
        den = filter_instance.den
        self.assertIsInstance(den, np.ndarray)
        self.assertEqual(len(den), 3)

    def test_wc(self):
        filter_instance = self.get_one()
        wc = filter_instance.wc
        self.assertIsInstance(wc, list)
        self.assertGreater(wc[1], wc[0])

    def test_delta_w(self):
        filter_instance = self.get_one()
        delta_w = filter_instance.delta_w
        self.assertIsInstance(delta_w, (int, float))


class test_HP(unittest.TestCase):
    def get_one(self, Too=1.1, m=0.2, w0=6000):
        return HP(Too, m, w0)

    def test_num(self):
        filter_instance = self.get_one()
        num = filter_instance.num
        self.assertIsInstance(num, np.ndarray)
        self.assertEqual(len(num), 3)

    def test_den(self):
        filter_instance = self.get_one()
        den = filter_instance.den
        self.assertIsInstance(den, np.ndarray)
        self.assertEqual(len(den), 3)

    def test_lti(self):
        filter_instance = self.get_one()
        lti = filter_instance.lti
        self.assertIsInstance(lti, scipy.signal.lti)

    def test_wr(self):
        filter_instance = self.get_one()
        wr = filter_instance.wr
        self.assertIsInstance(wr, (float, int))

    def test_MdB(self):
        filter_instance = self.get_one()
        MdB = filter_instance.MdB
        self.assertIsInstance(MdB, (float, int))


class test_Notch(unittest.TestCase):
    def get_one(self, T0=1.1, m=0.2, w0=6000):
        return Notch(T0, m, w0)

    def test_num(self):
        filter_instance = self.get_one()
        num = filter_instance.num
        self.assertIsInstance(num, np.ndarray)
        self.assertEqual(len(num), 3)

    def test_den(self):
        filter_instance = self.get_one()
        den = filter_instance.den
        self.assertIsInstance(den, np.ndarray)
        self.assertEqual(len(den), 3)

    def test_wc(self):
        filter_instance = self.get_one()
        wc = filter_instance.wc
        self.assertIsInstance(wc, list)
        self.assertGreater(wc[1], wc[0])

    def test_delta_w(self):
        filter_instance = self.get_one()
        delta_w = filter_instance.delta_w
        self.assertIsInstance(delta_w, (int, float))
