namespace backend.DTOs;
using System.Text.Json.Serialization;

public class AIClassificationDto
{
    [JsonPropertyName("classification")]
    public string Classification { get; set; } = "";
}