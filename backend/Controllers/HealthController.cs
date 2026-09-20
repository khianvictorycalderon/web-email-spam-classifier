using Microsoft.AspNetCore.Mvc;

[ApiController]
public class HealthController() : ControllerBase
{
    [HttpGet("/health")]
    public IActionResult TestHealth()
    {
        return Ok(new
        {
            Status = "Healthy"
        });
    }
}