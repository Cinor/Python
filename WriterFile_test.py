import csv
with open('output.csv', 'w', newline='') as csvfile:

  # 以空白分隔欄位，建立 CSV 檔寫入器
  writer = csv.writer(csvfile, delimiter=' ')

  writer.writerow(['姓名', '身高', '體重'])
  writer.writerow(['令狐沖', 175, 60])
  writer.writerow(['岳靈珊', 165, 57])