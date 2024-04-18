def get_formatter(name):
    if not name:
        name = 'stylish'
    module = __import__(f"gendiff.formatters.{name}", fromlist=[name])
    return module.format_string
