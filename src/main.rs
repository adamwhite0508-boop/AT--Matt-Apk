use eframe::egui;

enum AppScreen {
    Splash,
    Main,
}

struct ATApp {
    screen: AppScreen,
    drawer_open: bool,
}

impl Default for ATApp {
    fn default() -> Self {
        Self {
            screen: AppScreen::Splash,
            drawer_open: false,
        }
    }
}

impl eframe::App for ATApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        // TOP BAR - Main screen pe hi
        if matches!(self.screen, AppScreen::Main) {
            egui::TopBottomPanel::top("top_bar").show(ctx, |ui| {
                ui.horizontal(|ui| {
                    if ui.button("☰  AT World Matter").clicked() {
                        self.drawer_open = !self.drawer_open;
                    }
                    ui.with_layout(egui::Layout::right_to_left(egui::Align::Center), |ui| {
                        ui.label("⋮");
                    });
                });
            });

            // DRAWER - Left side
            if self.drawer_open {
                egui::SidePanel::left("drawer").exact_width(280.0).show(ctx, |ui| {
                    ui.vertical(|ui| {
                        // Header - Blue
                        egui::Frame::none().fill(egui::Color32::from_rgb(15, 102, 178)).show(ui, |ui| {
                            ui.set_min_height(200.0);
                            ui.vertical_centered(|ui| {
                                ui.add_space(20.0);
                                ui.label(egui::RichText::new("🛡️").size(60.0).color(egui::Color32::WHITE));
                                ui.label(egui::RichText::new("AT World Matter").size(20.0).strong().color(egui::Color32::WHITE));
                                ui.label(egui::RichText::new("WASM + RAKSHAK").size(12.0).color(egui::Color32::from_rgb(230,230,230)));
                            });
                        });

                        ui.add_space(10.0);
                        ui.separator();
                        
                        if ui.button("🧠  AT BRAIN AI").clicked() { self.drawer_open = false; }
                        if ui.button("🖼️  Photo Poster").clicked() { self.drawer_open = false; }
                        if ui.button("🛡️  AT CROWN Secure").clicked() { self.drawer_open = false; }
                        ui.separator();
                        if ui.button("ℹ️  About Us").clicked() { self.drawer_open = false; }
                    });
                });
            }
        }

        egui::CentralPanel::default().show(ctx, |ui| {
            match self.screen {
                AppScreen::Splash => {
                    ui.vertical_centered(|ui| {
                        ui.add_space(100.0);
                        // Banner Image Placeholder
                        ui.label(egui::RichText::new("AT WORLD MATTER\nBANNER").size(30.0).strong().color(egui::Color32::from_rgb(15, 102, 178)));
                        ui.add_space(200.0);
                        ui.label("WASM + RAKSHAK Platform");
                        ui.add_space(20.0);
                        if ui.add(egui::Button::new("Continue to AT World Matter").fill(egui::Color32::from_rgb(15, 102, 178))).clicked() {
                            self.screen = AppScreen::Main;
                        }
                    });
                }
                AppScreen::Main => {
                    ui.vertical_centered(|ui| {
                        ui.add_space(50.0);
                        ui.label(egui::RichText::new("✔").size(80.0).color(egui::Color32::from_rgb(15, 102, 178)));
                        ui.label(egui::RichText::new("Welcome to AT World Matter").size(24.0).strong());
                        ui.add_space(10.0);
                        ui.label(egui::RichText::new("WASM + RAKSHAK Platform Ready!").size(14.0).color(egui::Color32::GRAY));
                        ui.add_space(20.0);
                        ui.label("Rust Secure Build - All features working!");
                    });
                }
            }
        });
    }
}

fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "AT World Matter",
        options,
        Box::new(|_cc| Box::new(ATApp::default())),
    )
}
