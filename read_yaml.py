import yaml
import pandas as pd

result = None
output_filename_list = ['/home/salud/.eurobench/20210202_170725_136_69/subject_1/condition_01/run_01/run_01_pi_cov.yaml', '/home/salud/.eurobench/20210202_170725_136_69/subject_1/condition_01/run_01/run_01_pi_lnos.yaml', '/home/salud/.eurobench/20210202_170725_136_69/subject_1/condition_01/run_01/run_01_pi_mrom.yaml','/home/salud/.eurobench/20210202_170725_136_69/subject_1/condition_01/run_01/run_01_pi_cov.yaml']

for output_filename in output_filename_list:
    if '.yaml' in output_filename or '.yml' in output_filename:
        print('Open file')
        with open(output_filename, 'r') as stream:
            try:
                result = yaml.safe_load(stream)
                print('File opened')
            except yaml.YAMLError as exc:
                print ('Error')

    if result is not None:
        result_type = result['type']

        try:
            result_value = result['value']
        except:
            result_value = result['values']

        print (result_value)
        print (result_type)

        if result_type != 'scalar' and result_type != 'vector' and result_type != 'matrix' and result_type != 'vector_of_vector' and result_type != 'vector_of_matrix':
            result_data = None
            print ('Error')

        # transform to pandas format (it expects a list)
        if result_type == 'scalar' and isinstance(result_value, (int, float, complex)) and not isinstance(result_value, bool):
            number = result_value
            result_value = []
            result_value.append(number)

        # transform the data
        try:
            result_data = pd.DataFrame(result_value)
        except ValueError:
            result_data = None
            print ('Error')

        print ('Data transformed')

        if result_data is not None:
            print('Aggregate')

print('Bye')