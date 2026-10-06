# MobProg (CS0011) image-only slide content, transcribed by Claude from the slide pictures

Module 1
- p3 What is Android: Linux-based mobile OS; originally developed by Android Inc.; Google bought Android Inc. in 2005;
  open and free. Mind-map advantages: Open Source, Larger Developer and Community Reach, Increased Marketing,
  Inter App Integration, Reduced Cost of Development, Higher Success Ratio, Rich Development Environment.
- p4/p5: StatCounter line charts of Android and iOS version market share Jul 2024 to Jul 2025 (no exam facts beyond
  "Android 15/14 lead; iOS 18 leads").
- p6 version table (Version, Codename, Release year): 1.5 Cupcake 2009; 1.6 Donut 2009; 2.0-2.1 Eclair 2009;
  2.2 Froyo 2010; 2.3 Gingerbread 2010; 3.x Honeycomb 2011; 4.0 Ice Cream Sandwich 2011; 4.1-4.3 Jelly Bean 2012;
  4.4 KitKat 2013; 5.0-5.1 Lollipop 2014; 6 Marshmallow 2015; 7 Nougat 2016; 8 Oreo 2017; 9 Pie 2018; 10 = Android 10
  2019; 11 2020; 12 2021; 13 2023 (table says 13 for 2023 row and 14 for 2023 row; table is messy); 15 2024; 16 2025.
- p8 Android 1.0 and 1.1 (unnamed): first commercial versions, 2008 and 2009; first commercial device HTC Dream;
  1.0 alpha: Google Maps, Camera, Gmail/Contacts/Google sync, Web Browser, WiFi and Bluetooth; 1.1 beta: save
  attachment in message, reviews and details when searching businesses on Maps.
- p29 Android 16 "Baklava", June 10, 2025: Live Updates foundation (ProgressStyle notifications), Adaptive apps
  (large-screen resizability standard), Predictive Back (animations default; QPR2 introduced API 36.1).
- p30 slide TITLE says "Android 16" but the logo says 17: released June 16, 2026, internally "Cinnamon Bun":
  AppFunctions (apps expose structured functions to assistants and agents), Adaptive-first (resizable large-screen
  required for API 37 targets), Windowed interaction (App Bubbles, Bubble Bar, desktop PiP). Treat as Android 17.
- p31 reference chart of all versions with API levels (Android 1.0 API 1 ... 16 Baklava API 36, 17 Cinnamon Bun API 37).
- p32 Android Features: icons only (storage/database, multimedia, connectivity/wireless, messaging, apps, multi-touch).
- p34 Architecture stack (top to bottom) with components:
  Applications: Home, Contacts, Camera, SMS, Alarm, Time, Calendar, Music, Gallery, Phone, Clock, Email.
  Application Framework: Activity Manager, Package Manager, NFC Service, Location Service, Windows Manager,
  Notification Manager, Content Providers, View System.
  Android Runtime: Dalvik Virtual Machine, Zygote, Android Debug Bridge, Core Libraries.
  Platform Libraries: Media Framework, OpenGL, Graphics, SGL, SSL, SQLite, Surface Manager, FreeType.
  Linux Kernel: Display Driver, Wi-Fi Driver, Audio Driver, Bluetooth Driver, Camera Driver, USB Driver,
  Binder IPC Driver, Memory Driver.

Module 2
- p4 System requirements: screenshot of developer.android.com/studio requirements (no specific numbers legible).
- p7 New Project templates: No Activity, Empty Activity, Basic Views Activity, Bottom Navigation Views Activity,
  Empty Views Activity (selected), Navigation Drawer Views Activity, Game, C++.
- p8 New Project form: Name, Package name, Save location, Language (Java or Kotlin), Minimum SDK (list from API 16
  Android 4.1 Jelly Bean up; API 24 Android 7.0 Nougat selected).
- p9 IDE screenshot of MainActivity.java: `public class MainActivity extends AppCompatActivity { @Override protected
  void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState); setContentView(R.layout.activity_main); } }`
- p10 numbered interface parts 1-6 (toolbar, navigation bar, editor window, tool window bar, tool windows, status bar).

Module 3 code (Kotlin)
- p9: `var mutable = "Hello World" // can be changed`, `val immutable = 12 // cannot be changed`, `mutable = "Hi there"`.
- p10: `lateinit var str1 : String`, `var str2 : String? = null`, `str1 = "late init"`, println both.
- p11 if-else expression: `val greeting = if (time < 18) { "Good day." } else { "Good evening." }` and short form
  `val greeting = if (time < 18) "Good day." else "Good evening."` with `val time = 20` (prints Good evening.).
- p12 when: `val result = when (day) { 1 -> "Monday" ... 7 -> "Sunday" else -> "Invalid day." }`, day = 4 -> "Thursday".
- p13 loops: `val nums = arrayOf(1, 5, 10, 15, 20); for (x in nums) { println(x) }` and range `for (nums in 5..15)`.
- p14 class: `class Car { var brand = ""; var model = ""; var year = 0 }`, `val c1 = Car()`, set Ford/Mustang/1969.
- p15 constructor: `class Car(var brand: String, var model: String, var year: Int)`, `Car("Ford", "Mustang", 1969)`.
- p16 class functions: `fun drive() { println("Wrooom!") }`, `fun speed(maxSpeed: Int) { println("Max speed is: " + maxSpeed) }`,
  `c1.drive()`, `c1.speed(200)`.
- p17 init blocks: `class Person(val _name: String) { var name: String; init {...first...} init {...second...}
  init {...third...} init { this.name = _name; println("Name = $name") } }`; `Person("Abe")` prints first, second,
  third init block, then `Name = Abe` (init blocks run in order of appearance).
- p18 default values in primary constructor: `class employee(emp_id: Int = 100, emp_name: String = "abc")`;
  `employee(18018, "Sagnik")`, `employee(11011)` uses default name, `employee()` uses both defaults.
- p19 secondary constructors: `class Add { constructor(a: Int, b: Int) {...} constructor(a: Int, b: Int, c: Int) {...}
  constructor(a: Int, b: Int, c: Int, d: Int) {...} }`, `Add(5, 6)` -> "Sum of 5, 6 = 11" etc.
- p20 inheritance: `open class MyParentClass { val x = 5 }`, `class MyChildClass: MyParentClass() { fun myFunction()
  { println(x) } }` (classes are final by default; `open` allows inheritance).
- p23/p24 same onCreate in Kotlin vs Java: Kotlin `lateinit var textView: TextView`, `override fun onCreate(
  savedInstanceState: Bundle?)`, `textView = findViewById(R.id.text_view)`, `textView.text = "New Text"`;
  Java `TextView textView;`, `@Override public void onCreate(Bundle savedInstanceState)`,
  `textView = (TextView) findViewById(R.id.text_view);`, `textView.setText("New Text")`.
- p26 diagram: Java and Kotlin both compile to JVM bytecode (and decompile back).
- p27-p31 conversion example: Java MainActivity with `private TextView textView; private int count;` and
  `buttonOnClick` incrementing count; Kotlin result uses `private var textView: TextView? = null`,
  `private var count = 0`, `override fun onCreate(savedInstanceState: Bundle?)`, `count++`,
  `textView!!.text = Integer.toString(count)`. Shortcut Ctrl+Alt+Shift+K; dialog "Configure Kotlin with Android
  with Gradle": All modules, Kotlin compiler version (1.4.30-RC shown); changes build.gradle; .java becomes .kt.
- p33 Method 2 shows the "Kotlin not configured" banner with Configure link.

Module 4 code
- p6 `public class MainActivity extends Activity { }`
- p7 `public class MyService extends Service { }`
- p8 `public class MyReceiver extends BroadcastReceiver { public void onReceive(context, intent){} }`
- p9 `public class MyContentProvider extends ContentProvider { public void onCreate(){} }`
- p12 tree: MyProject/src/MyActivity.java; res/drawable/graphic.png; res/layout/main.xml, info.xml;
  res/mipmap/icon.png; res/values/strings.xml.
- p19 `ImageView imageView = (ImageView) findViewById(R.id.myimageview); imageView.setImageResource(R.drawable.myimage);`
- p20 strings.xml `<string name="hello">Hello, World!</string>`; `TextView msgTextView = (TextView) findViewById(R.id.msg);
  msgTextView.setText(R.string.hello);`
- p21 activity_main.xml: LinearLayout (fill_parent, orientation vertical) with TextView `@+id/text` "Hello, I am a
  TextView" and Button `@+id/button` "Hello, I am a Button" (wrap_content).
- p22 `public void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState);
  setContentView(R.layout.activity_main); }`
- p23 strings.xml with `<color name="opaque_red">#f00</color>` and `<string name="hello">Hello!</string>`; EditText uses
  `android:textColor="@color/opaque_red"` and `android:text="@string/hello"`.

Module 5
- p4 state diagram: Created -> Started -> Resumed <-> Paused -> Stopped -> Destroyed; Stopped -> Started (restart).
- p7 lifecycle flowchart: Activity launched -> onCreate() -> onStart() -> onResume() -> Activity running;
  another activity comes to foreground -> onPause(); user returns -> onResume(); activity no longer visible ->
  onStop(); user navigates back -> onRestart() -> onStart(); finishing or destroyed by system -> onDestroy() ->
  Activity shut down; apps with higher priority need memory -> App process killed (from onPause/onStop);
  user navigates to the activity -> onCreate().
- p9 `package com.jenkov.myfirstandroidapp; import android.app.Activity; ... public class MyFirstAndroidActivity extends Activity { }`
- p10 manifest: `<manifest> <application> <activity android:name=".ExampleActivity" /> </application> </manifest>`
- p11 `setContentView(R.layout.activity_main);`
- p13/p14 New Project: Empty Views Activity template; name, language Kotlin, Minimum SDK API 34, Finish.
- p15-p16 MainActivity.kt: `class MainActivity : AppCompatActivity()`, `override fun onCreate(savedInstanceState: Bundle?)`,
  `enableEdgeToEdge()`, `setContentView(R.layout.activity_main)`, `ViewCompat.setOnApplyWindowInsetsListener(...)`.
- p17-p18 activity_main.xml: `androidx.constraintlayout.widget.ConstraintLayout` (match_parent) with TextView
  "Hello Android!" constrained Bottom/End/Start/Top to parent.
