import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  static const String baseUrl = 'http://<YOUR_FLASK_IP>:5000/api';

  static Future<String> recommendCareer(String profile) async {
    final res = await http.post(Uri.parse('$baseUrl/recommend'),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"profile": profile}));
    return jsonDecode(res.body)["result"];
  }

  static Future<String> boostMood(String mood) async {
    final res = await http.post(Uri.parse('$baseUrl/mood'),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"mood": mood}));
    return jsonDecode(res.body)["result"];
  }

  static Future<String> suggestRecipe(String ingredient) async {
    final res = await http.post(Uri.parse('$baseUrl/recipe'),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"ingredient": ingredient}));
    return jsonDecode(res.body)["result"];
  }

  static Future<String> classifyEmail(String email) async {
    final res = await http.post(Uri.parse('$baseUrl/email'),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"text": email}));
    return jsonDecode(res.body)["result"];
  }
}
