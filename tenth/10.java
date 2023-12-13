import java.io.FileInputStream;
import java.io.FileOutputStream;
import jxl.Sheet;
import jxl.Workbook;
import jxl.write.Label;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import org.testng.annotations.*;
public class ExcelTest {
    @BeforeClass
    public void setUp() throws Exception {}
    @Test
    public void testExcel() throws Exception {
        FileInputStream fi = new FileInputStream("C:\\Users\\ST AND AUTOLAB\\excel\\Students.xls");
        Workbook workbook = Workbook.getWorkbook(fi);
        Sheet sheet = workbook.getSheet(0);
        FileOutputStream fo = new FileOutputStream("C:\\Users \\ST AND AUTOLAB\\excel\\Result.xls");
        WritableWorkbook wwb = Workbook.createWorkbook(fo);
        WritableSheet ws = wwb.createSheet("result1", 0); // writeable sheet
        Label resultLabel = new Label(6, 0, "Result");
        ws.addCell(resultLabel);
        for (int i = 1; i < sheet.getRows(); i++) {
            int score = Integer.parseInt(sheet.getCell(2, i).getContents());
            Label studentResultLabel = new Label(6, i, score > 35 ? "pass" : "fail");
            ws.addCell(studentResultLabel);
        }
        System.out.println("Records successfully updated");
        wwb.write();
        wwb.close();
    }
}
