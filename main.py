import os

def rename_files_in_directory(directory_path,prefix, suffix):
    """
    지정된 디렉토리 내의 모든 파일의 이름을 변경하고 저장합니다.
    확장자 앞에 접미사를 추가합니다.

    :param directory_path: 파일이 저장된 디렉토리의 경로
    :param suffix: 새 파일 이름의 접미사
    """
    # 디렉토리 내의 파일 목록을 가져옵니다.
    try:
        files = os.listdir(directory_path)
    except FileNotFoundError:
        print(f"Error: The directory {directory_path} does not exist.")
        return
    
    for filename in files:
        # 파일의 전체 경로를 구성합니다.
        old_file_path = os.path.join(directory_path, filename)

        # 파일이 아닌 경우는 무시합니다.
        if not os.path.isfile(old_file_path):
            continue
        
        # 파일 이름과 확장자를 분리합니다.
        name, ext = os.path.splitext(filename)

        # 새로운 파일 이름을 생성합니다.
        new_file_name = f"{prefix}{name}_{suffix}{ext}"
        new_file_path = os.path.join(directory_path, new_file_name)

        # 파일 이름을 변경합니다.
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} to {new_file_path}")

# 사용 예시
directory_path = './7'  # 경로
suffix = '8팀'  # 접미사
prefix = '코드 main' # 접두사
rename_files_in_directory(directory_path, prefix ,suffix)
