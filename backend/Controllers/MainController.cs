using Microsoft.AspNetCore.Mvc;
using backend.DTOs;

[ApiController]
public class MainController() : ControllerBase
{
    [HttpGet("/health")]
    public IActionResult TestHealth()
    {
        return Ok(new
        {
            Status = "Backend: Healthy"
        });
    }

    [HttpGet("/services/ai-service/health")]
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

    [HttpPost("api/ai-service/classify")]
    public async Task<IActionResult> ClassifyEmail(
        IConfiguration config,
        [FromBody] UserRequestDto req
    )
    {
        try
        {
            var aiUrl = config["Services:AI:Url"];
            using var client = new HttpClient();

            var res = await client.PostAsJsonAsync(
                $"{aiUrl}/api/classify",
                new { req.EmailContent }
            );

            res.EnsureSuccessStatusCode();

            var parsed = await res.Content.ReadFromJsonAsync<AIClassificationDto>();

            return Ok(parsed);
        } catch (Exception)
        {
            return StatusCode(500, new {});
        }
    }
}