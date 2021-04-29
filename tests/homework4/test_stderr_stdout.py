from homework4.task3.task import my_precious_logger


class TestStderrStdout:
    def test_stderr_log(self, capsys):
        """Testing that stderr equal 'error' if string start with that"""
        my_precious_logger("error")
        out, err = capsys.readouterr()
        assert err == "error"

    def test_stdout_log(self, capsys):
        """Testing that stdout equal string"""
        my_precious_logger("Ok")
        out, err = capsys.readouterr()
        assert out == "Ok"
