namespace backend.DTOs;
using System.Text.Json.Serialization;

public class AIClassificationDto
{
    [JsonPropertyName("classification")]
    public double Classification { get; set; }
}