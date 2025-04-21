import 'package:flutter/material.dart';
import '../services/api_service.dart';

class CareerScreen extends StatefulWidget {
  @override
  _CareerScreenState createState() => _CareerScreenState();
}

class _CareerScreenState extends State<CareerScreen> {
  final TextEditingController _controller = TextEditingController();
  String result = "";

  void fetchRecommendation() async {
    final res = await ApiService.recommendCareer(_controller.text);
    setState(() => result = res);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Career Recommendation')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: _controller, decoration: InputDecoration(labelText: "Your education background")),
            ElevatedButton(onPressed: fetchRecommendation, child: Text("Recommend")),
            SizedBox(height: 20),
            Text(result),
          ],
        ),
      ),
    );
  }
}
