# with open(user_created_dir, 'w', newline='', encoding='utf8') as csvfile:
#     writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow([self.tbl_wdt.horizontalHeaderItem(i).text() for i in range(self.tbl_wdt.columnCount())])
#     for i in range(self.tbl_wdt.rowCount()):
#         row = []
#         for j in range(self.tbl_wdt.columnCount()):
#             item = self.tbl_wdt.item(i, j)
#             if item is not None:
#                 row.append(item.text())
#         print(row)
#         writer.writerow(row)

