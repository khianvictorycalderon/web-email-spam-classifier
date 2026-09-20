using backend.Extensions;

// Building the API
var builder = WebApplication.CreateBuilder(args);

// Adding services
builder.Services.AddDefaultCorsPolicy(builder.Configuration);
builder.Services.AddControllers();

// Application
var app = builder.Build();

// Middlewares
app.UseCorsPolicy();
app.MapControllers();

// Running the main application
app.Run();