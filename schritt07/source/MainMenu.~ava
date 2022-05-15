import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

/**
 *
 * Main Menu fuer OOPong.
 *
 * @version 1.0 vom 12.05.2022
 * @flyxx 
 */

public class MainMenu extends JFrame {
  // Anfang Attribute
  // start attributes
  private JLabel jLabel1 = new JLabel("PONK!", SwingConstants.CENTER);   
  public JButton jbtn_play = new JButton();
  public JTextField jtf_wndw_height = new JTextField();
  public JTextField jtf_wndw_width = new JTextField();
  public JTextField jtf_ball_speed = new JTextField();
  public JButton jbtn_obstacles = new JButton();
  private JLabel jLabel2 = new JLabel("Spielfensterhoehe");
  private JLabel jLabel3 = new JLabel("Spielfensterbreite");
  private JLabel jLabel4 = new JLabel("Hindernisse");
  private JLabel jLabel5 = new JLabel("Ballgeschwindigkeit");
  private JLabel jLabel6 = new JLabel("Schlaegergeschwindigkeit");
  private JSeparator jSeparator1 = new JSeparator();
  public JButton jbtn_save_settings = new JButton();
  public JTextField jtf_paddle_speed = new JTextField();
  private JSeparator jSeparator2 = new JSeparator();
  private JLabel jLabel7 = new JLabel("Keybinds:", SwingConstants.CENTER);
  private JLabel jLabel8 = new JLabel(
          "<html><body>Linker Spieler:"
          + "<br><br>Schlaeger hoch: W;"
          + "<br><br>Schlaeger runter: S</body></html>"
  );
  private JLabel jLabel9 = new JLabel(
          "<html><body>Rechter Spieler:"
          + "<br><br>Schlaeger hoch: Pfeiltaste Hoch;"
          + "<br><br>Schlaeger runter: Pfeiltaste Runter</body></html>"
  );
  private JSeparator jSeparator3 = new JSeparator(SwingConstants.VERTICAL);
  // end attributes
  // Ende Attribute
  
  public MainMenu() { 
    // Frame-Initialisierung
    super();
    setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
    int frameWidth = 347; 
    int frameHeight = 545;
    setSize(frameWidth, frameHeight);
    Dimension d = Toolkit.getDefaultToolkit().getScreenSize();
    int x = (d.width - getSize().width) / 2;
    int y = (d.height - getSize().height) / 2;
    setLocation(x, y);
    setTitle("Ponk! - Main Menu");
    setResizable(false);
    Container cp = getContentPane();
    cp.setLayout(null);
    // Anfang Komponenten
    
    jbtn_play.setBounds(73, 74, 195, 57);
    jbtn_play.setText("Spielen!");
    jbtn_play.setFont(new Font("Arial", Font.PLAIN, 24));
    jbtn_play.setMargin(new Insets(2, 2, 2, 2));
    jbtn_play.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_play_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_play);
    jLabel1.setBounds(7, 3, 326, 60);
    jLabel1.setFont(new Font("Arial", Font.BOLD, 48));
    cp.add(jLabel1);
    jtf_wndw_height.setBounds(255, 160, 75, 20);

    jtf_wndw_width.setBounds(255, 190, 75, 20);

    jtf_ball_speed.setBounds(255, 250, 75, 20);

    jbtn_obstacles.setBounds(255, 215, 75, 25);

    jLabel2.setBounds(10, 160, 230, 20);

    jLabel3.setBounds(10, 190, 230, 20);

    jLabel4.setBounds(10, 220, 230, 20);

    jLabel5.setBounds(10, 250, 230, 20);
    
    jLabel6.setBounds(10, 280, 230, 20);

    jtf_wndw_height.setText("");
    cp.add(jtf_wndw_height);
    jtf_wndw_width.setText("");
    cp.add(jtf_wndw_width);
    jtf_ball_speed.setText("");
    cp.add(jtf_ball_speed);
    jbtn_obstacles.setText("Ein/Aus");
    jbtn_obstacles.setMargin(new Insets(2, 2, 2, 2));
    jbtn_obstacles.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_obstacles_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_obstacles);
    cp.add(jLabel2);
    cp.add(jLabel3);
    cp.add(jLabel4);
    cp.add(jLabel5);
    cp.add(jLabel6);
    
    jbtn_save_settings.setBounds(75, 310, 187, 25);
    jbtn_save_settings.setText("Einstellungen speichern");
    jbtn_save_settings.setMargin(new Insets(2, 2, 2, 2));
    jbtn_save_settings.addActionListener(new ActionListener() { 
      public void actionPerformed(ActionEvent evt) { 
        //jbtn_save_settings_ActionPerformed(evt);
      }
    });
    cp.add(jbtn_save_settings);
    
    // start components
    jtf_paddle_speed.setBounds(255, 280, 75, 20);
    jtf_paddle_speed.setText("");
    cp.add(jtf_paddle_speed);
    jLabel6.setBounds(10, 280, 230, 20);
    jSeparator1.setBounds(0, 143, 335, 10);
    cp.add(jSeparator1);
    jSeparator2.setBounds(0, 344, 329, 9);
    cp.add(jSeparator2);
    jLabel7.setBounds(72, 352, 190, 20);
    cp.add(jLabel7);
    jLabel8.setBounds(8, 392, 145, 89);
    cp.add(jLabel8);
    jLabel9.setBounds(184, 392, 145, 105);
    cp.add(jLabel9);
    jSeparator3.setBounds(168, 376, 9, 129);
    cp.add(jSeparator3);
    // end components
  } // end of public MainMenu
  
  // start methods
  
  // Anfang Methoden
  
  public static void main(String[] args) {
    MainMenu menu = new MainMenu();
    menu.setVisible(true);
  } // end of main
  
  public void jbtn_play_ActionPerformed(ActionEvent evt) {
    // TODO hier Quelltext einfuegen
    
  } // end of jbtn_play_ActionPerformed

  public void jbtn_obstacles_ActionPerformed(ActionEvent evt) {
    // TODO hier Quelltext einfuegen
    
  } // end of jbtn_obstacles_ActionPerformed

  public void jbtn_save_settings_ActionPerformed(ActionEvent evt) {
    // TODO add your code here
    
  } // end of jbtn_save_settings_ActionPerformed

  // end methods

  // Ende Methoden
} // end of class MainMenu

