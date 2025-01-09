import json
import argparse


def parse_list_file(file_path):
  """
    解析列表文件,将域名进行分类

    Args:
        file_path:列表文件路径

    Returns:
        包含了域名和域名后缀的元组
    """
  domains = []
  domain_suffixes = []
  with open(file_path, 'r') as file:
    for line in file:
      line = line.strip()
      if line:
        if line.startswith('+.'):
          domain_suffixes.append(line[2:])
        else:
          domains.append(line)
  return domains, domain_suffixes


def create_json_data(domains, domain_suffixes):
  """
    创建json数据

    Args:
        domains: 域名列表
        domain_suffixes:域名后缀列表
    Returns:
         json_data : 返回 json 对象
    """
  json_data = {
      "version":
          2,
      "rules": [
          {
              "domain": domains,
              "domain_suffix": domain_suffixes,
              "domain_keyword": [],
              "domain_regex": [],
              "source_ip_cidr": [],
              "ip_cidr": []
          }
      ]
  }
  return json_data


def write_json_file(json_data, output_file_path):
  """
    写入json到文件

    Args:
        json_data: json 数据
        output_file_path: 输出文件路径
    """
  with open(output_file_path, 'w') as outfile:
    json.dump(json_data, outfile, indent=2)


def main():
  """
       主函数

    解析命令行参数，并执行文件转换。
        默认输入文件在前，输出文件在后。
    """
  parser = argparse.ArgumentParser(
      description='Convert domain list file to JSON format.')
  parser.add_argument('input_file_path', type=str, help='Path to the input list file')
  parser.add_argument('output_file_path', type=str, help='Path to the output JSON file')
  args = parser.parse_args()

  domains, domain_suffixes = parse_list_file(args.input_file_path)
  json_data = create_json_data(domains, domain_suffixes)
  write_json_file(json_data, args.output_file_path)


if __name__ == "__main__":
  main()