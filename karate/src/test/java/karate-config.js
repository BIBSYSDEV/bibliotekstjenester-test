function setup() {
    const apiKey = java.lang.System.getenv("apiKey");
    return {
        ALMA_APIKEY: apiKey,
    };
}