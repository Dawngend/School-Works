# MobProg (CS0011) Midterm: Actual Questions (Modules 1 to 5)

Taken Wed Oct 7, 2026, 1 PM, on Canvas. Dawn pasted questions 1 to 18 (19 was cut off). Use as the STYLE and SCOPE
reference for future MobProg reviewers.

**Style:** mixed True/False, multiple choice, and typed fill-in (exact method names, e.g. `findViewById`,
`setContentView()` with parentheses, Kotlin `fun`). **Scope goes beyond the slides:** Logcat, RelativeLayout,
ListView/AdapterView, view IDs, PiP history, AOSP licensing, why setContentView belongs in onCreate.

1. `TextView myTextView = (TextView) ______(R.id.my_textview);` **findViewById**
2. T/F: You can create your layout in Android using HTML. Key given: **True** (via WebView/hybrid). Note: many course
   keys say False (layouts are XML or code); confirm with the prof's key.
3. UI elements drawn on-screen including buttons, lists, forms: **Views**
4. T/F: onResume() is called whenever the activity becomes visible. **False** (visible in onStart; onResume = foreground, interactive)
5. Method for fundamental setup (declare UI, member variables, configure UI): **onCreate()**
6. T/F: Setting content in onResume()/onStart() is inefficient because setContentView() is heavy. **True**
7. T/F: The core OS is AOSP, FOSS, primarily under the Apache License. **True**
8. Fill in: ______ loads the layout displayed on screen (with parentheses). **setContentView()**
9. Users can drag the PiP window to another location, starting in Android ___. **8**
10. T/F: Every view in a layout must have an ID. **False**
11. First lifecycle method called when the activity is created: **onCreate()**
12. T/F: Logcat displays logs from your device in real time to help debug. **True**
13. T/F: A layout determines how views are arranged. **True**
14. T/F: onCreate() and onDestroy() are called only once in the activity lifecycle. **True**
15. ViewGroup that positions children relative to each other or the parent: **Relative Layout**
16. Fill in: Kotlin keyword to declare a function: **fun**
17. T/F: In Kotlin, statements must end with a semicolon. **False**
18. T/F: A ListView is an AdapterView showing a vertical scrollable list, one view below the other. **True**
19. (cut off) "______ are additional files and static content that your code uses, such as bitmaps, layout
    definitions..." Expected: **Resources**
