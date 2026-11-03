use eframe::egui;

#[derive(Default)]
struct ATWorldApp { 
    name: String, 
    message: String 
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
            ui.add_space(10.0);
            ui.colored_label(egui::Color32::GREEN, &self.message);
        });
    }
}

#[cfg_attr(target_os="android", ndk_context::main)]
fn main() {
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "AT World Matter", 
        options, 
        Box::new(|_cc| Box::new(ATWorldApp::default()))
    ).unwrap();
}
