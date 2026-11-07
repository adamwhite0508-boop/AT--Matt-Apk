use eframe::egui;

#[derive(Default, PartialEq)]
enum Page { #[default] Home, Matter, About }

#[derive(Default)]
struct ATWorldApp {
    name: String,
    matter_code: String,
    matter_name: String,
    message: String,
    current_page: Page,
    matters: Vec<(String, String)>,
}

impl eframe::App for ATWorldApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::TopBottomPanel::top("top").show(ctx, |ui| {
            ui.horizontal(|ui| {
                ui.heading("AT WORLD MATTER");
                ui.separator();
                if ui.button("Home").clicked() { self.current_page = Page::Home; }
                if ui.button("Matter Entry").clicked() { self.current_page = Page::Matter; }
                if ui.button("About").clicked() { self.current_page = Page::About; }
            });
        });

        egui::CentralPanel::default().show(ctx, |ui| {
            match self.current_page {
                Page::Home => {
                    ui.vertical_centered(|ui| {
                        ui.add_space(20.0);
                        ui.heading("Welcome to AT WORLD");
                        ui.label("Sir, APK Successfully Ban Gaya!");
                        ui.add_space(10.0);
                        ui.horizontal(|ui| {
                            ui.label("Naam:");
                            ui.text_edit_singleline(&mut self.name);
                        });
                        if ui.button("Welcome Click").clicked() {
                            self.message = format!("Welcome {} Ji!", self.name);
                        }
                        ui.colored_label(egui::Color32::GREEN, &self.message);
                    });
                },
                Page::Matter => {
                    ui.heading("Matter Entry");
                    ui.separator();
                    ui.horizontal(|ui| {
                        ui.label("Matter Code:");
                        ui.text_edit_singleline(&mut self.matter_code);
                    });
                    ui.horizontal(|ui| {
                        ui.label("Matter Name:");
                        ui.text_edit_singleline(&mut self.matter_name);
                    });
                    if ui.button("Add Matter").clicked() {
                        if !self.matter_code.is_empty() {
                            self.matters.push((self.matter_code.clone(), self.matter_name.clone()));
                            self.matter_code.clear();
                            self.matter_name.clear();
                        }
                    }
                    ui.separator();
                    ui.label("Saved Matters:");
                    for (code, name) in &self.matters {
                        ui.label(format!("{} - {}", code, name));
                    }
                },
                Page::About => {
                    ui.heading("About AT World");
                    ui.label("AT WORLD MATTER - Full APK Version");
                    ui.label("Version 1.0 - Built with Rust + Egui");
                }
            }
        });
    }
}

#[cfg(target_os = "android")]
#[no_mangle]
pub fn android_main(_app: android_activity::AndroidApp) {
    android_logger::init_once(android_logger::Config::default().with_tag("at-world-matter"));
    let options = eframe::NativeOptions::default();
    let _ = eframe::run_native("AT World Matter", options, Box::new(|_cc| Ok(Box::new(ATWorldApp::default()))));
}

#[cfg(not(target_os = "android"))]
fn main() {
    let options = eframe::NativeOptions::default();
    eframe::run_native("AT World Matter", options, Box::new(|_cc| Ok(Box::new(ATWorldApp::default())))).unwrap();
}
