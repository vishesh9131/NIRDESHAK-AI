import 'package:flutter/material.dart';
import '../services/api_service.dart';

class MoodScreen extends StatefulWidget {
  @override
  _MoodScreenState createState() => _MoodScreenState();
}

class _MoodScreenState extends State<MoodScreen> {
  final TextEditingController _controller = TextEditingController();
  String result = "";

  void fetchMoodBoost() async {
    final res = await ApiService.boostMood(_controller.text);
    setState(() => result = res);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Mood Booster')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: _controller, decoration: InputDecoration(labelText: "Your current mood")),
            ElevatedButton(onPressed: fetchMoodBoost, child: Text("Boost My Mood")),
            SizedBox(height: 20),
            Text(result),
          ],
        ),
      ),
    );
  }
}
