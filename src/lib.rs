use eframe::egui;
#[derive(Default)]
struct ATWorldApp { name: String, message: String }
impl eframe::App for ATWorldApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("AT WORLD MATTER");
            ui.label("Sir, APK Successfully Ban Gaya!");
            ui.text_edit_singleline(&mut self.name);
            if ui.button("Click").clicked() { self.message = format!("Welcome {}", self.name); }
            ui.label(&self.message);
        });
    }
}
#[cfg_attr(target_os="android", ndk_context::main)]
fn main() {
    eframe::run_native("AT World Matter", eframe::NativeOptions::default(), Box::new(|_cc| Box::new(ATWorldApp::default()))).unwrap();
}
