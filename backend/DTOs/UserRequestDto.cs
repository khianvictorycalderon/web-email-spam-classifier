namespace backend.DTOs;
using System.Text.Json.Serialization;

public class UserRequestDto
{
    [JsonPropertyName("email_content")]
    public string EmailContent { get; set; } = "";
}