
//import com.intuit.karate.Results;
//import com.intuit.karate.Runner;
//import org.junit.jupiter.api.Test;
//import static org.junit.jupiter.api.Assertions.assertEquals;

import com.intuit.karate.junit5.Karate;

public class SRUTest {

    @Karate.Test
    Karate testAll() {
        return Karate.run().relativeTo(getClass());
    }

//    @Test
//    void test() {
//        Results results = Runner.path("classpath:/")
//                .outputCucumberJson(true).parallel(1);
//        assertEquals(0, results.getFailCount(), results.getErrorMessages());
//    }

}
