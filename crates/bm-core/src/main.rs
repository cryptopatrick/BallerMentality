use poem::{listener::TcpListener, Route, Server};
use poem_openapi::{payload::PlainText, OpenApi, OpenApiService};

struct Api;

#[OpenApi]
impl Api {
    /// Hello World
    #[oai(path="/", method = "get")]
    async fn index(&self) -> PlainText<&'static str> {
        PlainText("Hello World!")
    }
}

#[tokio::main]
async fn main() {
    let api_service = 
        OpenApiService::new(Api, "Hello World", "1.0").server("http://localhost:3000");
    let ui = api_service.swagger_ui();
    let app = Route::new().nest("/", api_service).nest("/docs", ui);

    Server::new(TcpListener::bind("127.0.0.1:3000"))
        .run(app)
        .await;

    // tracing_subscriber::fmt::init();
}