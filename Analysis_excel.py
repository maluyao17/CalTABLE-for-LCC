import pandas as pd

def Analysis():
    input_file = "计算结果.xlsx"
    df = pd.read_excel(input_file)

    category_columns = ["项目类别", "项目目的", "供电分区"]
    x_column = "单位投资效益"
    results = {}


    for category in category_columns:
        category_values = df[category].unique()
        category_result = {}
        for value in category_values:
            filtered_rows = df[df[category] == value]
            x_values = filtered_rows[x_column]
            
            max_x = x_values.max()
            min_x = x_values.min()
            avg_x = x_values.mean()
            median_x = x_values.median()

            category_result[value] = {
                "最大值 X": max_x,
                "最小值 X": min_x,
                "平均值 X": avg_x,
                "中位数 X": median_x
            }
        results[category] = category_result

    output_file = "统计分析结果.xlsx"
    with pd.ExcelWriter(output_file) as writer:
        for category, category_result in results.items():
            df_result = pd.DataFrame.from_dict(category_result, orient="index")
            df_result.to_excel(writer, sheet_name=category)

    print(f"结果已保存到 {output_file}")
