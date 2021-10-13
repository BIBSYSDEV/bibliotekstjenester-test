function fn() {
    const apiKey = java.lang.System.getenv("apiKey");
    karate.log(apiKey);
    return {
        ALMA_APIKEY: apiKey,
    };
}