package tests.sandbox;

import com.intuit.karate.Results;
import com.intuit.karate.Runner;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@Tag("sandbox")
public class SandboxKarateRunnerIT {

    @Test
    void runAllFeaturesInSpecificDirectory() {{
        Results results = Runner.path("classpath:sandbox_tests")
                              .outputCucumberJson(true)
                              .parallel(1);
        assertEquals(0, results.getFailCount(), results.getErrorMessages());
    }}

}