import 'package:flutter_test/flutter_test.dart';
import 'package:mindmate_ai/main.dart';

void main() {
  testWidgets('MindMate app starts', (WidgetTester tester) async {
    await tester.pumpWidget(const MindMateApp());
    expect(find.text('MindMate AI'), findsWidgets);
  });
}
