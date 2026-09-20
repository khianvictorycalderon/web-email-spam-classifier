namespace backend.Extensions;

public static class CorsExtension {
    public static IServiceCollection AddDefaultCorsPolicy(
        this IServiceCollection services,
        IConfiguration configuration
    )
    {
        var allowedOrigins = configuration
            .GetSection("Cors:AllowedOrigins").Get<string[]>() ?? [];

        services.AddCors(options =>
        {
            options.AddDefaultPolicy(policy =>
            {
                policy
                    .AllowAnyHeader()
                    .AllowAnyMethod()
                    .WithOrigins(allowedOrigins);
            });
        });

        return services;
    }

    public static IApplicationBuilder UseCorsPolicy(
        this IApplicationBuilder app
    )
    {
        app.UseCors();
        return app;
    }
}