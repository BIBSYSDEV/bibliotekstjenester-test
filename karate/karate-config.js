function fn() {
    const apiKey = java.lang.System.getenv("apiKey");
    karate.log(apiKey.testPrimoApiKey);
    return {
        ALMA_APIKEY: apiKey.testPrimoApiKey,
    };
}