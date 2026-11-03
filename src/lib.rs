use eframe::egui;

#[derive(Default)]
struct ATWorldApp {
    name: String,
    message: String,
}

impl eframe::App for ATWorldApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("AT WORLD MATTER");
            ui.separator();
            ui.label("Sir, APK Successfully Ban Gaya!");
            ui.add_space(10.0);
            ui.horizontal(|ui| {
                ui.label("Naam:");
                ui.text_edit_singleline(&mut self.name);
            });
            if ui.button("Click to Test").clicked() {
                self.message = format!("Welcome {}!", self.name);
            }
            ui.label(&self.message);
        });
    }
}

#[cfg(target_os = "android")]
#[no_mangle]
fn android_main(app: winit::platform::android::activity::AndroidApp) {
    android_logger::init_once(android_logger::Config::default().with_max_level(log::LevelFilter::Info));
    let options = eframe::NativeOptions { renderer: eframe::Renderer::Glow, android_app: Some(app), ..Default::default() };
    eframe::run_native("AT World Matter", options, Box::new(|_cc| Box::new(ATWorldApp::default()))).unwrap();
}

#[cfg(not(target_os = "android"))]
fn main() {
    let options = eframe::NativeOptions { renderer: eframe::Renderer::Glow, ..Default::default() };
    eframe::run_native("AT World Matter", options, Box::new(|_cc| Box::new(ATWorldApp::default()))).unwrap();
}
