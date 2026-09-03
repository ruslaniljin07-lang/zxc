import subprocess
import sys
import os
import tempfile


def _run_python_code(code, timeout=5):
    """Execute code in subprocess with full UTF-8 support."""
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.py', delete=False, encoding='utf-8'
        ) as f:
            f.write(code)
            temp_path = f.name

        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'

        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True, text=True, encoding='utf-8',
            timeout=timeout, cwd=os.path.dirname(temp_path), env=env
        )
        os.unlink(temp_path)

        return {
            'success': result.returncode == 0,
            'returncode': result.returncode,
            'stdout': result.stdout,
            'stderr': result.stderr
        }
    except subprocess.TimeoutExpired:
        if temp_path:
            try:
                os.unlink(temp_path)
            except OSError:
                pass
        return {
            'success': False, 'returncode': None,
            'stdout': '',
            'stderr': 'Превышено время выполнения (5 секунд).'
        }
    except Exception as e:
        return {
            'success': False, 'returncode': None,
            'stdout': '',
            'stderr': 'Ошибка при выполнении: ' + str(e)
        }


def check_code(user_code, test_code, timeout=5):
    full_code = user_code + '\n' + test_code
    return _run_python_code(full_code, timeout)


def run_sandbox_code(code, timeout=5):
    return _run_python_code(code, timeout)
