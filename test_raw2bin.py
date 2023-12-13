from os.path import abspath, dirname, join
from suite2p import default_ops, run_s2p


_dir_raw = abspath(join(dirname(__file__), 'raw'))


def test():
    ops = default_ops()
    ops['input_format'] = 'raw'
    run_s2p(ops=ops, db=dict(data_path=[_dir_raw]))


'__main__' == __name__ and test()
