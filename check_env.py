"""
check_env.py
Simple environment checker to validate critical package versions.
Run with the virtualenv active: `python check_env.py`
"""
import sys

def get_ver(pkg_name):
    try:
        m = __import__(pkg_name)
        return getattr(m, '__version__', 'unknown')
    except Exception:
        return None

pkgs = ['django', 'sklearn', 'joblib', 'pandas', 'numpy', 'requests', 'httpx']

print('Python:', sys.version.splitlines()[0])
for p in pkgs:
    v = get_ver(p)
    if v is None:
        print(f"{p}: NOT INSTALLED")
    else:
        print(f"{p}: {v}")

# check sklearn compatibility
sk = get_ver('sklearn')
if sk and sk.split('.')[0:2] != ['1','5'] and sk != 'unknown':
    print('\nWarning: installed scikit-learn version may not match saved model version (1.5.0).')
    print('If you see InconsistentVersionWarning when unpickling models, consider:')
    print('  pip install scikit-learn==1.5.0')
