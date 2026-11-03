use eframe::egui;
use winit::platform::android::activity::AndroidApp;

#[derive(Default)]
struct ATApp { page: String }

impl eframe::App for ATApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("AT WORLD MATTER - Rust Secure");
            ui.separator();
            if ui.button("AT BRAIN AI").clicked() { self.page = "BRAIN".into(); }
            if ui.button("Photo Poster").clicked() { self.page = "POSTER".into(); }
            if ui.button("AT CROWN Secure").clicked() { self.page = "CROWN".into(); }
            ui.label(format!("Current: {}", self.page));
        });
    }
}

#[cfg(target_os = "android")]
#[no_mangle]
fn android_main(_app: AndroidApp) {
    let options = eframe::NativeOptions { renderer: eframe::Renderer::Glow, ..Default::default() };
    eframe::run_native("AT World Matter", options, Box::new(|_cc| Box::new(ATApp::default()))).unwrap();
}
