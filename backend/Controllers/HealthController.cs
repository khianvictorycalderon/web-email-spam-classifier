using Microsoft.AspNetCore.Mvc;
using backend.DTOs;

[ApiController]
public class HealthController() : ControllerBase
{
    [HttpGet("/health")]
    public IActionResult TestHealth()
    {
        return Ok(new
        {
            Status = "Backend: Healthy"
        });
    }

    [HttpGet("/ai-service/health")]
    public async Task<IActionResult> TestAIServiceHealth(
        IConfiguration config
    )
    {
        try
        {
            var aiUrl = config["Services:AI:Url"];
            using var client = new HttpClient();

            var res = await client.GetAsync(
                $"{aiUrl}/health"
            );

            res.EnsureSuccessStatusCode();

            var parsed = await res.Content.ReadFromJsonAsync<AIHealthResponseDto>();

            return Ok(parsed);
        } catch (Exception)
        {
            return StatusCode(500, new {});
        }
    }
}