from enum import Enum
import sys
import json


class ExecCommand:
    class Command(Enum):
        Locate = ("locate", "_filter_by_location")
        Find_price_hourly_lte = ("find_price_hourly_lte", "_filter_by_hourly_rate_lte")
        Find_price_hourly_gt = ("find_price_hourly_gt", "_filter_by_hourly_rate_gte")

        @staticmethod
        def get_filter_function(str_command):
            for command in ExecCommand.Command:
                if command.value[0] == str_command:
                    return command.value[1]
            raise Exception(
                "Invalid Command <{0}>, Please refer to read me for the available commands".format(str_command))

    def __init__(self, file: str):
        input_data = load_data(file)
        if not input_data or type(input_data) != list:
            raise Exception("the data is not in the expected format")
        self.data = input_data

    def execute(self, command, token):
        function_name = self.Command.get_filter_function(str_command=command)
        return getattr(self, function_name)(token)

    def _filter_by_location(self, token):
        return [x['name'] for x in filter(lambda x: x['address']['state'] == token, self.data)]

    def _filter_by_hourly_rate_lte(self, token):
        return [x['name'] for x in filter(lambda x: x['price_hourly'] <= int(token), self.data)]

    def _filter_by_hourly_rate_gte(self, token):
        return [x['name'] for x in filter(lambda x: x['price_hourly'] > int(token), self.data)]


def load_data(path):
    try:
        with open(path) as file:
            data = json.load(file)
            file.close()
            return data
    except FileNotFoundError:
        raise Exception("The file path does not seems to be valid.")
    except Exception as e:
        raise Exception("Something went wrong while loading the file : " + str(e))


def evaluate(file, command, token):
    execCommand = ExecCommand(file)
    result = execCommand.execute(command, token)
    print(", ".join(result))
    return


if __name__ == '__main__':
    args = sys.argv
    if (len(args) != 4):
        print("Invalid execution command Please refer to README for the exact format")
    else:
        file = args[1]
        command = args[2]
        token = args[3]
        try:
            evaluate(file, command, token)
        except Exception as e:
            print("Exception occured : " + str(e))
