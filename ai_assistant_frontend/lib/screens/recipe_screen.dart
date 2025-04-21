import 'package:flutter/material.dart';
import '../services/api_service.dart';

class RecipeScreen extends StatefulWidget {
  @override
  _RecipeScreenState createState() => _RecipeScreenState();
}

class _RecipeScreenState extends State<RecipeScreen> {
  final TextEditingController _controller = TextEditingController();
  String result = "";

  void fetchRecipe() async {
    final res = await ApiService.suggestRecipe(_controller.text);
    setState(() => result = res);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Recipe Suggestion')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(controller: _controller, decoration: InputDecoration(labelText: "Enter an ingredient")),
            ElevatedButton(onPressed: fetchRecipe, child: Text("Suggest Recipe")),
            SizedBox(height: 20),
            Text(result),
          ],
        ),
      ),
    );
  }
}
