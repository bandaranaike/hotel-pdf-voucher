from datetime import datetime
import env


def run(func, params):
    try:
        func(params)
    except AssertionError as e:
        log_message("AssertionError : ", e)
    except AttributeError as e:
        log_message("AttributeError : ", e)
    except EOFError as e:
        log_message("EOFError : ", e)
    except FloatingPointError as e:
        log_message("FloatingPointError : ", e)
    except GeneratorExit as e:
        log_message("GeneratorExit : ", e)
    except ImportError as e:
        log_message("ImportError : ", e)
    except IndexError as e:
        log_message("IndexError : ", e)
    except KeyError as e:
        log_message("KeyError : ", e)
    except KeyboardInterrupt as e:
        log_message("KeyboardInterrupt : ", e)
    except MemoryError as e:
        log_message("MemoryError : ", e)
    except NameError as e:
        log_message("NameError : ", e)
    except NotImplementedError as e:
        log_message("NotImplementedError : ", e)
    except OSError as e:
        log_message(e)
    except OverflowError as e:
        log_message("OverflowError : ", e)
    except ReferenceError as e:
        log_message("ReferenceError : ", e)
    except RuntimeError as e:
        log_message("RuntimeError : ", e)
    except StopIteration as e:
        log_message("StopIteration : ", e)
    except SyntaxError as e:
        log_message("SyntaxError : ", e)
    except SystemError as e:
        log_message("SystemError : ", e)
    except SystemExit as e:
        log_message("SystemExit : ", e)
    except TypeError as e:
        log_message("TypeError : ", e)
    except UnicodeError as e:
        log_message("UnicodeError : ", e)
    except ValueError as e:
        log_message("ValueError : ", e)
    except ZeroDivisionError as e:
        log_message("ZeroDivisionError : ", e)
    except Exception as e:
        log_message(e)


def log_message(*message):
    file = open('log.txt', 'a')
    file.write(str(datetime.now()))
    file.write(" : ")
    file.write(str(message[0]))
    file.write(str(message[1]))
    file.write("\n")
    file.close()
