import 'package:flutter/material.dart';
import 'career_screen.dart';
import 'mood_screen.dart';
import 'recipe_screen.dart';
import 'email_screen.dart';

class HomeScreen extends StatelessWidget {
  void navigate(BuildContext context, Widget screen) {
    Navigator.push(context, MaterialPageRoute(builder: (_) => screen));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('AI Assistant')),
      body: ListView(
        children: [
          ListTile(title: Text('Career Recommendation'), onTap: () => navigate(context, CareerScreen())),
          ListTile(title: Text('Mood Booster'), onTap: () => navigate(context, MoodScreen())),
          ListTile(title: Text('Recipe Suggestion'), onTap: () => navigate(context, RecipeScreen())),
          ListTile(title: Text('Email Classification'), onTap: () => navigate(context, EmailScreen())),
        ],
      ),
    );
  }
}
