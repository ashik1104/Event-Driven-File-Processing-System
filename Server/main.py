import glob
import shutil
import os
import traceback

source_path = '../Source/*'
destination_path = '../Destination'

postfixes = [1, 2, 3]

while True:
    source_files = glob.glob(source_path)
    # print('source folder files : ', source_files)

    try:
        if len(source_files) > 0:
            target_file_path = source_files[0]
            # print('target file path : ', target_file_path)

            shutil.copy(target_file_path, '.')  # copy the target file to the server folder where we are coding

            file_name_in_source = target_file_path.split('\\')[-1]
            splited_file_name = file_name_in_source.split('.')

            if splited_file_name[-1] == 'py':
                with open(f'{file_name_in_source}', mode='r', encoding='utf-8') as hello:
                    code = hello.read()
                    exec(code)
                hello.close()
                os.remove(target_file_path)  # removing python file from source
                os.remove(file_name_in_source)  # removing python file from Server
            else:
                print('file name : ', file_name_in_source)
                prefix = splited_file_name[0]
                postfix = splited_file_name[1]

                path = os.path.join('.', 'package')
                os.mkdir(path)

                for item in range(len(postfixes)):
                    file_name = prefix + '_' + str(item + 1) + '.' + postfix
                    print(file_name)
                    with open(f'{file_name_in_source}', 'r') as file1, open('test.txt', 'w') as file2:
                        lines = file1.readlines()
                        for i in range((item + 1) * 10):
                            file2.write(lines[i])
                    shutil.move('test.txt', f'./package/{file_name}')

                shutil.make_archive('zip_files', 'zip', root_dir='package')
                shutil.move('zip_files.zip', f'{destination_path}')
                shutil.unpack_archive(f'{destination_path}/zip_files.zip',
                                      extract_dir=f'{destination_path}/Extracted_files',
                                      format='zip')
                d_files = glob.glob('../Server/package/*')
                for f in d_files:
                    os.remove(f)
                os.remove(target_file_path)  # removing text file from source
                os.remove(file_name_in_source)  # removing text file from Server
                os.remove(f'{destination_path}/zip_files.zip')  # removing zip file from destination
                shutil.rmtree('package')


    except Exception as e:
        print(traceback.format_exc())
        print(e, 'error has occurred')
        shutil.rmtree('package')
        a = '../Source/*'
        b = glob.glob(a)
        c = b[0]
        os.remove(c)
        d_files = glob.glob('../Server/*')
        for f in d_files:
            if (f.split('\\')[-1].split('.')[-1] == 'txt') or (
                    f.split('\\')[-1].split('.')[-1] == 'py' and f.split('\\')[-1].split('.')[0] != 'main'):
                os.remove(f)
