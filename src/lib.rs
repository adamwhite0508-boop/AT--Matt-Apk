use eframe::egui;
use std::io::Write;

#[derive(Default)]
struct App {
    name: String,
    counter: i32,
    slider: f32,
    checked: bool,
}

impl eframe::App for App {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("AT World Matter");
            ui.separator();
            ui.label("Welcome! App chal raha hai.");
            ui.separator();
            ui.horizontal(|ui| {
                ui.label("Name:");
                ui.text_edit_singleline(&mut self.name);
            });
            ui.separator();
            if ui.button(format!("Click Count: {}", self.counter)).clicked() {
                self.counter += 1;
            }
            ui.separator();
            ui.add(egui::Slider::new(&mut self.slider, 0.0..=100.0).text("Slider"));
            ui.separator();
            ui.checkbox(&mut self.checked, "Enable Feature");
            if self.checked {
                ui.label(format!("Hello {} Slider = {}", self.name, self.slider));
            }
        });
    }
}

fn write_crash_log(msg: &str) {
    if let Ok(mut f) = std::fs::File::create("/sdcard/Download/crash_log.txt") {
        let _ = f.write_all(msg.as_bytes());
    }
}

fn setup_crash_log() {
    std::panic::set_hook(Box::new(|info| {
        let payload = if let Some(s) = info.payload().downcast_ref::<&str>() {
            s.to_string()
        } else if let Some(s) = info.payload().downcast_ref::<String>() {
            s.clone()
        } else {
            "unknown panic".to_string()
        };
        let loc = info.location().map(|l| format!("{} {} {}", l.file(), l.line(), l.column())).unwrap_or("unknown".to_string());
        let msg = format!("AT_MATT CRASH Error: {} Location: {}", payload, loc);
        write_crash_log(&msg);
    }));
}

#[cfg(target_os = "android")]
use android_logger::Config;
#[cfg(target_os = "android")]
use android_activity::AndroidApp;
#[cfg(target_os = "android")]
use winit::platform::android::EventLoopBuilderExtAndroid;

#[cfg(target_os = "android")]
#[no_mangle]
pub fn android_main(app: AndroidApp) {
    setup_crash_log();
    android_logger::init_once(Config::default().with_tag("AT_MATT"));
    write_crash_log("AT_MATT STARTED");

    let options = eframe::NativeOptions {
        event_loop_builder: Some(Box::new(move |builder| {
            builder.with_android_app(app.clone());
        })),
        ..Default::default()
    };

    let result = eframe::run_native(
        "AT World Matter",
        options,
        Box::new(|_cc| Ok(Box::<App>::default())),
    );

    if let Err(e) = result {
        let msg = format!("AT_MATT RUN_NATIVE FAILED Error: {}", e);
        write_crash_log(&msg);
    }
}

#[cfg(not(target_os = "android"))]
fn main() {
    setup_crash_log();
    let options = eframe::NativeOptions::default();
    let _ = eframe::run_native(
        "AT World Matter",
        options,
        Box::new(|_cc| Ok(Box::<App>::default())),
    );
}
