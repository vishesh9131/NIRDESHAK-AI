import 'package:flutter/material.dart';
import '../services/api_service.dart';

class EmailScreen extends StatefulWidget {
  @override
  _EmailScreenState createState() => _EmailScreenState();
}

class _EmailScreenState extends State<EmailScreen> {
  final TextEditingController _controller = TextEditingController();
  String result = "";

  void classifyEmail() async {
    final res = await ApiService.classifyEmail(_controller.text);
    setState(() => result = res);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Email Classifier')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              decoration: InputDecoration(labelText: "Paste email content"),
              maxLines: 6,
            ),
            ElevatedButton(onPressed: classifyEmail, child: Text("Classify")),
            SizedBox(height: 20),
            Text("Result: $result"),
          ],
        ),
      ),
    );
  }
}
