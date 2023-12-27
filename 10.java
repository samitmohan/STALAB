// Check off module-info option while making project
// Add paths correctly to excel sheets and add build path -> selenium and jar files
import java.io.*;
import jxl.*;
import jxl.write.*;

public class p10 {
    public void test() throws Exception {
        FileInputStream fi = new FileInputStream("students.xls");
        Workbook workbook = Workbook.getWorkbook(fi);
        Sheet sheet = workbook.getSheet(0);
        FileOutputStream fo = new FileOutputStream("results.xls");
        WritableWorkbook wwb = Workbook.createWorkbook(fo);
        WritableSheet ws = wwb.createSheet("result1", 0);
        Label resultLabel = new Label(6, 0, "Result");
        ws.addCell(resultLabel);
        for (int i = 1; i < sheet.getRows(); i++) {
            int score = Integer.parseInt(sheet.getCell(2, i).getContents());
            Label studentResult = new Label(6, i, score > 35 ? "pass" : "fail");
            ws.addCell(studentResult);
        }
        System.out.println("Records successfully updated");
        wwb.write();
        wwb.close();
        fi.close();
        fo.close();
    }
}
